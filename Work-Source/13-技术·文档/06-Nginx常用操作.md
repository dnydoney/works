# 技术·文档 | Nginx常用操作
-----------------------------------------------------------------

1、 安装环境： Centos7

2、安装所需插件：

```
    yum -y install gcc

    yum install -y pcre pcre-devel

    yum install -y zlib zlib-devel

    yum install -y openssl openssl-devel

```

3、安装nginx

```
    wget http://nginx.org/download/nginx-1.9.9.tar.gz  

    tar -zxvf  nginx-1.9.9.tar.gz

    切换到cd /下载目录/nginx-1.9.9/下面，执行下面三个指令

    ./configure
 
    make

    make install

```

4、切换到/usr/local/nginx安装目录

5、配置nginx的配置文件nginx.conf文件，主要也就是端口

6、启动nginx服务
```
	切换目录到/usr/local/nginx/sbin下面，执行下面启动指令
	
	./nginx
	
```
7、查看nginx服务是否启动成功

```
	切换目录到/usr/local/nginx/sbin下面，执行下面启动指令
	
	ps -ef | grep nginx
	
```
8、Nginx二级域名指向NodeJs

```
server {
        listen       80;
        #域名
        server_name  blog.huruji3.com;

        location / {
             #node.js应用的端口
             proxy_pass http://127.0.0.1:3001;
             root blog;
       }
        #静态文件交给Nginx直接处理
        location ~ *^.+\.(css | js | txt | swf | mp4)$ {
            root E:\huruji\blog\wechat_v1.1\public;
             access_log off;
            expires 24h;
       }
    }
```