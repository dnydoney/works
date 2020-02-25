###  2020年02月23日

-----------------------------------------------------------------

### Running the samples

#### iOS / Android

```
cd <sample_directory>
flutter run 
```

#### Web

Make sure you're on Flutter version "Flutter 1.12.13+hotfix.6 • channel beta" or newer. Not all samples support web at this time, so please check the sample directory for a `lib/main_web.dart` file.

```
cd <sample_directory>
flutter run -d chrome -t lib/main_web.dart
```



###  2020年02月23日

-----------------------------------------------------------------

`Flutter GO for web` 的代码库



- git 拉取 `Flutter-go` 项目,并切换到 `web/flutter-go-web-0.0.1` 分支

```
  $ git clone -b web/flutter-go-web-0.0.1 https://github.com/alibaba/flutter-go.git flutter-go-web
```

- 安装flutter_web构建工具

```
  $ flutter pub global activate webdev
```

- 更新pub[**包**]()

```
  $ pub get

  //... 
  Resolving dependencies... 
Warning: You are using these overridden dependencies:
! flutter_web 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web
! flutter_web_test 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web_test
! flutter_web_ui 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web_ui
Got dependencies!
Precompiling executables... (12.0s)
```

- 开发模式,获取（无状态）热重载 webdev

```
  $ webdev serve --auto restart

  [INFO] Building new asset graph completed, took 2.0s
  [INFO] Checking for unexpected pre-existing outputs. completed, took 1ms
  [INFO] Serving `web` on http://127.0.0.1:8080
  [INFO] Running build completed, took 49.7s
  [INFO] Caching finalized dependency graph completed, took 421ms
  [INFO] Succeeded after 50.1s with 3309 outputs (9338 actions)
```

- 浏览器打开 [http://127.0.0.1:8080](http://127.0.0.1:8080/)
- 发布模式,创建最终编译结果,这将创建一个build目录`index.html`，`main.dart.js`以及使用静态HTTP服务器运行应用程序所需的其余文件。

```
  $ webdev build
```





### 



###  2020年02月21日

-----------------------------------------------------------------

不要使用`pub get`或`pub upgrade`命令来管理你的依赖关系。相反，应该使用`flutter packages get`或`flutter packages upgrade`。如果您想手动使用pub，则可以通过设置`FLUTTER_ROOT`环境变量来直接运行它。

## 升级 Flutter channel 和 packages

要同时更新Flutter SDK和你的依赖包，在你的应用程序根目录（包含`pubspec.yaml`文件的目录）中运行`flutter upgrade` 命令:

```shell
$ flutter upgrade
```

## 升级你的依赖包

如果您修改了`pubspec.yaml`文件，或者只想更新应用依赖的包(不包括Flutter SDK)，请使用以下命令：

- `flutter packages get`获取`pubspec.yaml`文件中列出的所有依赖包
- `flutter packages upgrade` 获取`pubspec.yaml`文件中列出的所有依赖包的最新版本





###  2020年02月21日

-----------------------------------------------------------------



要查看您当前使用的分支，请运行`flutter channel`查看。

要切换分支，请使用`flutter channel beta` 或 `flutter channel master`




    1、本地Flutter SDK 版本 1.9.1+hotfix.6 。
    2、pubspec.yaml 中的第三方包版本和 pubspec.lock 中的是否对应的上ps 1.12.x 版本请切换到 dev_next 分支



试一试下面这行代码切换到dev分支
`flutter channel dev`
然后
`flutter version`
打印出所有版本
选择其中某个版本,进行切换，比如
`flutter version v1.7.8+hotfix.4`



flutter doctor -v






    $ flutter channel
      Flutter channels:
        *   stable
            beta
            dev
            master
```

flutter pub get

packages get
packages upgrade
flutter upgrade
flutter clean
```


 flutter go，官方的指南版本如下：
1.版本version/channel切换问题

```
    flutter channel beta
    flutter version v1.7.8 + hotfix.4
 

	flutter pub cache repair
    
    flutter channel dev_next 
    flutter version 1.9.1+hotfix.6
    
```

2.将项目适配到web端
```
	flutter create .
```
3.运行到web上 && 运行到android上

```
    flutter run -d chrome
    flutter run -d android
```





###  2020年02月16日

-----------------------------------------------------------------

常用命令

1.编译：

​		flutter packages get: 获取flutter packages包

2.运行：

​		flutter run （默认为debug环境）
​		flutter run --release (以release模式运行)

3.安装

​		帮助：flutter -h 或 flutter --help
​		诊断flutter：flutter doctor
​		查看flutter版本号：flutter --version
​		flutter升级：flutter upgrade

4.打包apk包：

​		直接打包： flutter build apk
​		64位-release： flutter build apk --release --target-platform android-arm64
​		32位-release： flutter build apk --release --target-platform android-arm



编译、运行、发布

```
git clone https://github.com/creatint/light
flutter pub cache repair
flutter packages get
flutter packages upgrade
flutter run
flutter build apk --release
```

Gradle 配置国内阿里云的maven库地址


```

    buildscript {  
      repositories {   
         maven { url 'https://maven.aliyun.com/repository/google' } 
         maven { url 'https://maven.aliyun.com/repository/jcenter' }  
         maven { url 'http://maven.aliyun.com/nexus/content/groups/public' } 
      }  
      dependencies {  
          classpath 'com.android.tools.build:gradle:3.5.3'              
   
       }
    }
    allprojects { 
       repositories {  
          maven { url 'https://maven.aliyun.com/repository/google' }  
          maven { url 'https://maven.aliyun.com/repository/jcenter' }  
          maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }  
          }
    }

```





### 几个flutter常用命令

以下是常用命令：

| 常用命令             | 含义                                    |
| -------------------- | --------------------------------------- |
| **--version**        | 查看Flutter版本                         |
| **-h**或者**--help** | 打印所有命令行用法信息                  |
| analyze              | 分析项目的Dart代码。                    |
| **build**            | Flutter构建命令。                       |
| channel              | 列表或开关Flutter通道。                 |
| clean                | 删除构建/目录。                         |
| config               | 配置Flutter设置。                       |
| **create**           | 创建一个新的Flutter项目。               |
| **devices**          | 列出所有连接的设备。                    |
| **doctor**           | 展示了有关安装工具的信息。              |
| drive                | 为当前项目运行Flutter驱动程序测试。     |
| format               | 格式一个或多个Dart文件。                |
| fuchsia_reload       | 在Fuchsia上进行热重载。                 |
| **help**             | 显示帮助信息的Flutter。                 |
| **install**          | 在附加设备上安装Flutter应用程序。       |
| logs                 | 显示用于运行Flutter应用程序的日志输出。 |
| packages             | 命令用于管理Flutter包。                 |
| precache             | 填充了Flutter工具的二进制工件缓存。     |
| run                  | 在附加设备上运行你的Flutter应用程序。   |
| screenshot           | 从一个连接的设备截图。                  |
| stop                 | 停止在附加设备上的Flutter应用。         |
| test                 | 对当前项目的Flutter单元测试。           |
| trace                | 开始并停止跟踪运行的Flutter应用程序。   |
| **upgrade**          | 升级你的Flutter副本。                   |



 ###  学习随笔
-----------------------------------------------------------------

