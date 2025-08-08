# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import time
from wangyiyun_comments.items import *
from dbutils.pooled_db import PooledDB

# 创建全局连接池（避免每个管道独立连接）
mysql_pool = PooledDB(
    creator=pymysql,
    host='localhost',
    user='root',
    password='',
    database='wangyiyun',
    charset='utf8mb4',
    maxconnections=10,  # 控制最大连接数
    autocommit=False # 自动提交
)

# 歌单写入数据库
class WangyiyunTOPLISTPipeline:
    def open_spider(self, spider):
        self.conn = mysql_pool.connection()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

    def process_item(self, item, spider):
        if isinstance(item, WangyiyunTOPItem):
            topSQL = 'INSERT IGNORE INTO TOPLIST(list_name,list_id) VALUES(%s,%s)'
            try:
                self.cursor.execute(topSQL, (item['toplist_name'], item['toplist_id']))
                self.conn.commit()  # 每次插入后提交
            except Exception as e:
                self.conn.rollback()
                spider.logger.error(f"插入歌单失败: {e}")
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# 歌曲写入数据库
class SongPipeline():
    def __init__(self):
        self.songs = []
        self.songs_long = 50
        self.last_commit_time = time.time()  # 添加时间戳

    def open_spider(self, spider):
        self.conn = mysql_pool.connection()
        self.cursor = self.conn.cursor()
        # 设置锁等待超时时间（秒）
        self.cursor.execute("SET SESSION innodb_lock_wait_timeout = 30")
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

    def process_item(self, item, spider):
        if isinstance(item, WangyiyunSONGItem):
            self.songs.append((
                item['songname'],
                item['songid'],
                item['singer'],
                item['songs_url'],
                item['toplist_id'],
            ))

            # 条件1：达到批量大小  条件2：每30秒强制提交一次（防止少量数据长时间不提交）
            if len(self.songs) >= self.songs_long or time.time() - self.last_commit_time > 30:
                self.insert_info()
        return item

    def insert_info(self):
        try:
            # 使用INSERT IGNORE避免主键冲突导致的锁
            songSQL = 'INSERT IGNORE INTO song(songname,songid,singer,song_url,list_id) VALUES(%s,%s,%s,%s,%s)'
            self.cursor.executemany(songSQL, self.songs)
            self.conn.commit()
            self.songs.clear()
            self.last_commit_time = time.time()  # 更新提交时间
        except Exception as e:
            self.conn.rollback()
            # 记录错误但不停止爬虫
            spider.logger.error(f"批量插入歌曲失败: {e}")

    def close_spider(self, spider):
        if self.songs:
            try:
                self.insert_info()
            except Exception as e:
                spider.logger.error(f"关闭时插入失败: {e}")
        self.cursor.close()
        self.conn.close()

# 评论
class CommentPipeline:
    def __init__(self):
        self.comment_buffer = []
        self.batch_size = 200
        self.last_commit_time = time.time()

    def open_spider(self, spider):
        # 从连接池获取连接
        self.conn = mysql_pool.connection()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SET SESSION innodb_lock_wait_timeout = 30") # 30缓冲
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

    def process_item(self, item, spider):
        if isinstance(item, WangyiyunCOMMENTSItem):
            self.comment_buffer.append((
                item['songid'],
                item['comment_name'],
                item['comment_ip'],
                item['comment_content'],
            ))

            # 批量提交条件：数量或时间
            if len(self.comment_buffer) >= self.batch_size or time.time() - self.last_commit_time > 30:
                self.insert_batch()
        return item

    def insert_batch(self):
        try:
            commentsql = "INSERT IGNORE INTO comments (songid,comment_name, comment_ip, comment_content) VALUES (%s, %s, %s, %s)"
            self.cursor.executemany(commentsql, self.comment_buffer)
            self.conn.commit()
            self.comment_buffer.clear()
            self.last_commit_time = time.time()
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"批量插入评论失败: {e}")

    def close_spider(self, spider):
        if self.comment_buffer:
            try:
                self.insert_batch()
            except Exception as e:
                spider.logger.error(f"关闭时插入评论失败: {e}")
        self.cursor.close()
        self.conn.close()  # 这里返还给连接池