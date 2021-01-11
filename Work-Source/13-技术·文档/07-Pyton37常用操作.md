# 技术·文档 | Python37常用操作
-----------------------------------------------------------------

1、 安装环境： Centos7

2、安装所需插件：

```
    yum -y install gcc

    yum install -y pcre pcre-devel

    yum install -y zlib zlib-devel

    yum install -y openssl openssl-devel

    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel kernel-devel libffi-devel

```

3、安装python37

```
    weget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz

    tar -Jxvf Python-3.9.0.tar.xz

    切换到cd Python-3.9.0，执行下面指令

    ./configure prefix=/usr/local/python3
 
    make

    make install

```

4、设置快捷方式


```
 设置软链接：ln -s /root/python3 /usr/bin/python3
```

ln -s /usr/local/python3 /root/python3