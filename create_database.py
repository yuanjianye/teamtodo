#!/usr/bin/python
import MySQLdb

conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="Jiawm5535",port=3306)
cur=conn.cursor()

conn.select_db('teamtodo')
#cur.execute('create table test(id int,info varchar(20))')

create_table_commands = ["""CREATE TABLE `tb_todolist` (
`todo_id`       int(10)         unsigned    NOT NULL    AUTO_INCREMENT,
`user_name`       int(10)         unsigned    NOT NULL,
`group_id`      int(10)         unsigned    NOT NULL,
`todo_content`  varchar(255)                NOT NULL    DEFAULT '',
`todo_add_date` datetime                                default NULL,
`todo_status`   int(4)          unsigned    NOT NULL    default 0,
PRIMARY KEY (`todo_id`)
)
""" ,
"""CREATE TABLE `tb_user` (
`user_name`     varchar(255)                NOT NULL,
`user_passwd`   varchar(255)                NOT NULL,
`user_status`   int(4)          unsigned    NOT NULL    default 0,
PRIMARY KEY (`user_name`)
)
""" ,
"""CREATE TABLE `tb_group` (
`group_id`      int(10)         unsigned    NOT NULL    AUTO_INCREMENT,
`group_name`    varchar(255)                NOT NULL,
`group_creater` int(10)         unsigned    NOT NULL,
`group_manager` int(4)          unsigned    NOT NULL    default 0,
PRIMARY KEY (`group_id`)
)
""" ,
"""CREATE TABLE `tb_belong` (
`belong_id`     int(10)         unsigned    NOT NULL    AUTO_INCREMENT,
`user_name`       int(10)         unsigned    NOT NULL,
`group_id`      int(10)         unsigned    NOT NULL,
PRIMARY KEY (`belong_id`)
)
""" ,
"""CREATE TABLE `tb_operation` (
`operation_id`      int(10)     unsigned    NOT NULL    AUTO_INCREMENT,
`operation_content` varchar(255)            NOT NULL,
`todo_id`           int(10)     unsigned    NOT NULL,
`operation_date`    datetime                            default NULL,
PRIMARY KEY (`operation_id`)
)
"""] 
#print create_table_commands
for sql in create_table_commands:
    print sql
    cur.execute(sql)
    conn.commit()
    cur.close
    conn.close



    #cur.execute('create database if not exists python')
    #conn.select_db('python')
    #cur.execute('create table test(id int,info varchar(20))')

    #value=[1,'hi rollen']
    #cur.execute('insert into test values(%s,%s)',value)

    #values=[]
    #for i in range(20):
        #values.append((i,'hi rollen'+str(i)))

    #cur.executemany('insert into test values(%s,%s)',values)

    #cur.execute('update test set info="I am rollen" where id=3')

    #conn.commit()
    #cur.close()
    #conn.close()
