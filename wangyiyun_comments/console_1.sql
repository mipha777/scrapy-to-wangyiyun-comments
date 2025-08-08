create database wangyiyun charset 'utf8';

use wangyiyun;
create table if not exists toplist(
    id int primary key auto_increment,
    list_name varchar(255) not null ,
    list_id varchar(255) not null
);

desc toplist;

ALTER TABLE toplist ADD UNIQUE(list_id);


create table if not exists song(
    id int primary key auto_increment,
    songname varchar(255) not null ,
    songid varchar(255) not null unique,
    singer varchar(255) not null ,
    song_url varchar(255) not null ,
    list_id varchar(255) not null  ,
    constraint fk_parent FOREIGN KEY(list_id) references toplist(list_id)
);
drop table toplist;
drop table song;
drop table comments;
select * from toplist;
select * from song;

create table if not exists comments(
    id int primary key auto_increment,
    songid varchar(255) not null ,
    comment_name varchar(255) not null ,
    comment_ip varchar(255) not null ,
    comment_content varchar(500) not null,
    constraint fk_son foreign key (songid) references song(songid)
);



desc comments;
select * from comments;
#       comment_name = scrapy.Field()
#     comment_ip = scrapy.Field()
#     comment_content = scrapy.Field()
#     songid = scrapy.Field()# 外键链接歌曲id

