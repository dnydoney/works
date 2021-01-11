# 技术·文档 | Electron开发指南
-----------------------------------------------------------------

1、 安装环境： Centos7，Mysql5.7

2、启动命令

```
  # 进入工程目录 
  # 提升安装速度，使用国内镜像
  npm config set registry https://registry.npm.taobao.org
  npm install
  npm run dev
```

3、常用命令

```
  # 进入工程目录 
  # 开发者模式
  npm run dev

  # 生产者模式
  npm run start

  # 打包-windows版本
  npm run build-w

  # 打包-mac版本
  npm run build-m

  # 打包-linux版本
  npm run build-l

  # web运行-开发模式
  npm run web-dev

  # web运行-生产者模式-启动
  npm run web-start

  # web运行-生产者模式-停止
  npm run web-stop
  
```

4、运行命令
```
  # 运行开发模式
  npm run dev:web
  npm run dev:exe

  # 打包安装文件 
  npm run build:web
  npm run build:exe
  
```

5、项目结构
```
  - build 打包图标
  - layout 前端文件
    - public
    - src
   - src
  - main 主线程目录
  - renderer 渲染线程（前端打包输出目录）
  
```

