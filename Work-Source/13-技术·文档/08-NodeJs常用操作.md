# 技术·文档 | NodeJs常用操作
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

3、安装NodeJs

```
    wget https://nodejs.org/dist/latest/node-v15.5.0-linux-x64.tar.xz      

    tar -Jxvf node-v15.5.0-linux-x64.tar.xz 

	移动并改名文件夹

    cd /usr/local/
    
    mv /root/ms100/tools/node-v15.5.0-linux-x64 . //后面的.表示移动到当前目录
    
    mv node-v15.5.0-linux-x64/ nodejs

```

4、让npm和node命令全局生效


```
 　方式一：环境变量方式（这种方式似乎只对登录用户有效？）

　　1）、加入环境变量，在 /etc/profile 文件末尾增加配置

    vi /ect/profile
    export PATH=$PATH:/usr/local/nodejs/bin
　　2）、执行命令使配置文件生效

	source /etc/profile
　　方式二：软链接方式（推荐）

    ln -s /usr/local/nodejs/bin/npm /usr/local/bin/
    ln -s /usr/local/nodejs/bin/node /usr/local/bin/
 
 
```

5、Putty上执行后台运行命令失效


```
 　 nohup命令失效，关闭putty后无法在后台运行
    用putty连接ubuntu，要执行一个后台命令
    正常用nohup直接运行命令，就可以在后台运行
    nohup ./1.sh &


    但关闭putty后，发现命令也停止了


    问题出在，直接点putty的右上角X关闭按钮，nohup也会停止


    解决：直接在putty中输入exit退出即可
 
 
```
