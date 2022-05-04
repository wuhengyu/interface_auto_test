CREATE TABLE `test_case_list1`(
`id` INT(255) NOT NULL AUTO_INCREMENT,
`web` VARCHAR(255) DEFAULT NULL,
`module` VARCHAR(255) DEFAULT NULL,
`title` VARCHAR(255) DEFAULT NULL,
`url` VARCHAR(255) DEFAULT NULL,
`method` VARCHAR(255) DEFAULT NULL,
`headers` VARCHAR(255) DEFAULT NULL,
`cookies` VARCHAR(255) DEFAULT NULL,
`request_body` TEXT DEFAULT NULL,
`request_type` VARCHAR(255) DEFAULT NULL,
`relation` VARCHAR(255) DEFAULT NULL,
`expected_code` VARCHAR(255) DEFAULT NULL,
`isdel` VARCHAR(255) DEFAULT NULL,
PRIMARY KEY(`id`) USING BTREE
) ENGINE=INNODB;

#插入第一条测试用例
INSERT INTO `test_case_list` (`id`, `web`, `module`, `title`, `url`, `method`, `headers`, `cookies`, `request_body`, `request_type`, `relation`, `expected_code`, `isdel`)
VALUES(1,'zrlog','登录模块','密码错误','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":\"admin\",\"password\":123456,\"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第二条测试用例
INSERT INTO `test_case_list`
VALUES (2,'zrlog','登录模块','不携带密码参数','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":\"admin\",\"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第三条测试用例
INSERT INTO `test_case_list`
VALUES (3,'zrlog','登录模块','用户名错误','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":\"adminadminadminadmin\",\"password\":\"ca72de92e7e1767aefe5853a282836e7\",1
"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第四条测试用例
INSERT INTO `test_case_list`
VALUES (4,'zrlog','登录模块','用户名为非字符串类型','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":123,\"password\":\"ca72de92e7e1767aefe5853a282836e7\",1
"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第五条测试用例
INSERT INTO `test_case_list`
VALUES (5,'zrlog','登录模块','用户名为非字符串类型','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"password\":\"ca72de92e7e1767aefe5853a282836e7\",1
"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第六条测试用例
INSERT INTO `test_case_list`
VALUES (6,'zrlog','登录模块','用户名为空字符串','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":\“\”,\"password\":\"ca72de92e7e1767aefe5853a282836e7\",1
"https\":False,\"key\":1598188173501}','json', NULL,'1', 1);
#插入第七条测试用例
INSERT INTO `test_case_list`
VALUES (7,'zrlog','登录模块','用户名和密码正确','/api/admin/login','post',
'{\"Content-Type\"：\"application/json\"}','{}',
'{\"userName\":\“admin\”,\"password\":\"ca72de92e7e1767aefe5853a282836e7\",1
"https\":False,\"key\":1598188173501}','json', 'token=cookies.admin-token','0', 1);
#插入第八条测试用例
INSERT INTO `test_case_list`
VALUES (8,'zrlog','文章管理模块','发布文章','/api/admin/article/create','post',
'{\"Content-Type\":\"application/json\"}','{\"admin-token\":\"${token}\"}',
'{\"id\":None,\"editorType\":\"markdown\",\"title\":\"付出\",\"alias\":\"付出\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":None,
\"cancomment\":False,\"recommended\":False,\"privacy\":
False,\"content\":\"<p>付出</p >\\n\",\"markdown\":\"付出\",\"rubbish\":False}','json','id_name=body.id,alias_name=body.alias','O', 1);
#插入第九条测试用例
INSERT INTO `test_case_list`
VALUES (9,'zrlog','文章管理模块','修改文章','/api/admin/article/update','post',
'{\"Content-Type\":\"application/json\"}','{\"admin-token\":\"${token}\"}',
'{\"id\":\"${id_name}\",\"editorType\":\"markdown\",\"title\":\"付出才能杰出\",\"alias\":\"${alias_name}\",\"thumbnail
\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":\"<p>付出</p>\",
\"cancomment\":False,\"recommended\":False,\"privacy\":
False,\"content\":\"<p>付出</p >\\n\",\"markdown\":\"付出\",\"rubbish\":False}','json',NULL,'O', 1);
#插入第十条测试用例
INSERT INTO `test_case_list`
VALUES (10,'zrlog','文章管理模块','删除文章','/api/admin/article/delete','post',
'{\"Content-Type\":\"application/x-www-form-urlencoded\"}','{\"admin-token\":\"${token}\"}',
'{\"oper\":\"del\",\"id\":\"${id_name}\"}','data','NULL','0', 1);
#插入第十一条测试用例
INSERT INTO `test_case_list`
VALUES (11,'zrlog','文章管理模块','查询文章','/api/admin/article?keywords=付出才能杰出&_search=false&nd=1598429806679&rows=10&page=1&sidx=
&sord=asc','get','{\"Content-Type\":\"application/x-www-form-urlencoded\"}','{\"admin-token\":\"${token}\"}','{}','data', NULL,'O', 1);

create table `test_config`(
    `id` int(0) NOT NULL,
    `web` varchar(255) default null,
    `key` varchar(255) default null,
    `value` varchar(255) default null,
    primary key (`id`) using btree
) ENGINE = InnoDB;

CREATE TABLE `test_result_record`(
`id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT,
`case_id` varchar(255) DEFAULT NULL,
`times` varchar(255) DEFAULT NULL,
`response` varchar(1000) DEFAULT NULL COMMENT '实际结果',
`result` varchar(255) default NULL,
primary key (`id`) using btree
)engine =InnoDB;
