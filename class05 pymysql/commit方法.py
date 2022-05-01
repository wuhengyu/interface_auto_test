# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 19:17
# @Author  : Walter
# @File    : commit方法.py
# @License : (C)Copyright Walter
# @Desc    :
import pymysql

db = pymysql.Connect(
    host='localhost',
    user='root',
    password='123456',
    database='ZrLog',
    charset='utf8',
    port=3306
)

cursor = db.cursor()
for _ in range(1000):
    _ += 1
    print(f'正在插入第{_}条数据')
    sql = "INSERT INTO `ZrLog`.`log` (`canComment`, `click`, `version`, `content`, `plain_content`, `markdown`, `digest`, `keywords`, `thumbnail`, `recommended`, `releaseTime`, `last_update_date`, `title`, `typeId`, `userId`, `hot`, `rubbish`, `privacy`, `editor_type`) VALUES (b'1', 2, 0, '<blockquote>\n<p>Hello World 中文意思是『世界，你好』。因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，所以后来的程序员在学习编程或进行设备调试时延续了这一习惯</p>\n</blockquote>\n<p>ZrLog是使用Java开发的博客/CMS程序，具有简约，易用，组件化，内存占用低等特点。自带Markdown编辑器，让更多的精力放在写作上，而不是花费大量时间在学习程序的使用上</p>\n<p>现在你可以通过访问 <a href=\"/zrlog/admin/article-edit?id=1\">admin</a> 编辑或删除这篇文章，然后开始愉快的写作吧</p>\n', 'Hello World 中文意思是『世界，你好』。因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，所以后来的程序员在学习编程或进行设备调试时延续了这一习惯 ZrLog是使用Java开发的博客/CMS程序，具有简约，易用，组件化，内存占用低等特点。自带Markdown编辑器，让更多的精力放在写作上，而不是花费大量时间在学习程序的使用上 现在你可以通过访问 admin 编辑或删除这篇文章，然后开始愉快的写作吧', '> Hello World 中文意思是『世界，你好』。因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，所以后来的程序员在学习编程或进行设备调试时延续了这一习惯\n\nZrLog是使用Java开发的博客/CMS程序，具有简约，易用，组件化，内存占用低等特点。自带Markdown编辑器，让更多的精力放在写作上，而不是花费大量时间在学习程序的使用上\n\n现在你可以通过访问 [admin](/zrlog/admin/article-edit?id=1) 编辑或删除这篇文章，然后开始愉快的写作吧', '<p>Hello World 中文意思是『世界，你好』。因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，所以后来的程序员在学习编程或进行设备调试时延续了这一习惯</p><p>ZrLog是使用Java开发的博客/CMS程序，具有简约，易用，组件化，内存占用低等特点。自带Markdown编辑器，让更多的精力放在写作上，而不是花费大量时间在学习程序的使用上</p> ...', '记录', NULL, b'0', '2022-05-01 10:51:46', '2022-05-01 10:51:46', %s, 1, 1, NULL, b'0', b'0', NULL);"
    value = (f'测试{_}')
    cursor.execute(sql, value)
    # 提交数据
    db.commit()
cursor.close()
db.close()
