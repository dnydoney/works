
###  2020年02月21日
-----------------------------------------------------------------




    1、本地Flutter SDK 版本 1.9.1+hotfix.6 。
    2、pubspec.yaml 中的第三方包版本和 pubspec.lock 中的是否对应的上ps 1.12.x 版本请切换到 dev_next 分支



试一试下面这行代码切换到dev分支
`flutter channel dev`
然后
`flutter version`
打印出所有版本
选择其中某个版本,进行切换，比如
`flutter version v1.7.8+hotfix.4`






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





 ###  学习随笔
-----------------------------------------------------------------

