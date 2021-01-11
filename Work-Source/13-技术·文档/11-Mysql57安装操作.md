# 技术·文档 | Nginx SSL添加操作
-----------------------------------------------------------------

1、 安装环境： Centos7，Mysql5.7

2、下载命令：

```
  wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
```

3、yum源安装：

```
  rpm -ivh mysql57-community-release-el7-9.noarch.rpm
```

4、安装完成后，就可以使用yum命令安装mysql了：


```
yum -y install mysql-server
```

5、启动mysql


```
 systemctl start mysqld
```
5、查看mysql状态

``` 
systemctl status mysqld   
```
6、获取mysql的临时密码

```
grep 'temporary password' /var/log/mysqld.log	
```

7、登录mysql

```
  mysql -uroot -p
```

8、修改新密码

```
ALTER USER 'root'@'localhost' IDENTIFIED BY '新的密码';
```

9、降低密码安全强度

```
set global validate_password_policy=0;--表示将密码安全等级设置为low
set global validate_password_length=6;--表示将密码长度设置为最小6位
```

9、授权远程访问数据库

```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '新密码' WITH GRANT OPTION;
flush privileges;
```