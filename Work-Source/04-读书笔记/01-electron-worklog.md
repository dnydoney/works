

###  2020年02月16日
-----------------------------------------------------------------
1. 安装路径

    ```
    npm install --ELECTRON_MIRROR="https://cdn.npm.taobao.org/dist/electron/"
    ```

2. 编译打包成.exe

   ```
   npm install save-dev electron-packager
   ```
3. package.json中配置打包命令

    "scripts": {
        "start": "electron .",
        "package:win": "electron-packager . myClient --win --out ../myClient --arch=x64 --app-version=0.0.1 --electron-version=2.0.0"
      },


    　　

        “.”：需要打包的应用目录（即当前目录），
        “myClient”：应用名称，
        “--win”：打包平台（以Windows为例），
        “--out ../myClient”：输出目录，
        “--arch=64”：64位，
        “--app-version=0.0.1”：应用版本，
        “--electron-version=2.0.0”：electron版本



使用淘宝镜像，否则会一直卡在那

\> electron-quick-start@1.0.0 package:win E:\myObject\my\netObject\electron-hello\electron-quick-start
\> electron-packager . myClient --win --out ../myClient --arch=x64 --app-version=0.0.1 --electron-version=2.0.0

```
npm run package:win --ELECTRON_MIRROR="https://cdn.npm.taobao.org/dist/electron/"
```



### 开发模式

```
npm run dev
```

### 编译打包

```
npm run build
```



 ###  Electron学习笔记
-----------------------------------------------------------------

