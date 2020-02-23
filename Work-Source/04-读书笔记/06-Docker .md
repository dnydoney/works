##  Docker安装

```
1、Docker要求CentOS系统的内核版本高于3.10，通过uname -r命令查看你当前的内核版本
uname -r

2、使用 root 权限登录Centos。确保yum包更新到最新。
yum update

3、卸载旧版本(如果安装过旧版本的话)
yum remove docker  docker-common docker-selinux docker-engine

4、安装需要的软件包，yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的
yum install -y yum-utils device-mapper-persistent-data lvm2

5、设置yum源
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

6、安装docker
yum install docker-ce  #由于repo中默认只开启stable仓库，故这里安装的是最新稳定版

7、启动并加入开机启动
systemctl start docker
systemctl enable docker

8、验证安装是否成功(有client和service两部分表示docker安装启动都成功了)
```



###  构建镜像并启动：

```
1、创建mysql数据持久化目录
mkdir /data

2、运行mysql镜像
docker run --name mysql -v /data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD="test@123" -e MYSQL_DATABASE="omms" -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

