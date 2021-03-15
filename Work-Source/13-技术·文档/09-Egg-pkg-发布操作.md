# 技术·文档 | Egg打包发布常用操作
-----------------------------------------------------------------

1、 安装环境： Centos7

2、安装所需插件：

```
   npm install pkg -g
```

3、配置Egg.js的public路径

```
   // 修改config/config.default.js
   config.static = {
      prefix: '/',
      dir: process.cwd() + '/public'
   }

```

4、配置Egg.js的运行时路径


```
  //修改config/config.default.js
  config.rundir = process.cwd() + '/run'
 
```

5、修改package.json配置pkg相关参数：


```
//修改package.json，增加pkg节点
"pkg": {
"assets": [
    "./config/*.js",
    "./app.js",
    "./app/**/*.js",
    "./node_modules/**/*.js"  //该行为必须添加，由于Egg.js使用nanoid库，其中用				到一个文件pkg未能解析，于是手动添加
    ]
}

```
5、根目录下，创建build.js，配置pkg入口：
``` 
   'use strict';
    // build.js文件内容
    require(__dirname + '/node_modules/egg-scripts/bin/egg-scripts.js');
 
```
6、配置pkg入口：
```
   // 修改package.json，增加bin节点，指定入口文件
    "bin": "build.js" 
```

7、配置build命令
```
       // 修改package.json,在scripts下增加build命令
    "scripts": {
        "build": "pkg . --targets node8-linux-x64 --out-path /usr/dist  		--debug"
      }
    // --targets 指定node版本为8以及linux-x64
    // --out-path 指定打包后文件输出路径
    // --debug 指定debug模式编译
 
```

8、开始打包
```
    // 初次打包时间较长，后续打包pkg会使用node缓存，提高打包效率
    npm run build
 
```

9、运行
```
    ./test_pkg start /snapshot/test_pkg --port=9001 --title=test_pkg
    // ./test_pkg 打包后的二进制文件
    // /snapshot/test_pkg 其中/snapshot为必须路径，test_pkg为工程目录路径
    // --port --title等支持与平常启动时的任意命令参数
 
```

9、更多打包细节，参见
```
    https://github.com/MrSmallLiu/pkg-egg-example 
```