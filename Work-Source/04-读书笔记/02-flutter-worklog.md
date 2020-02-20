

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
flutter packages get
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

