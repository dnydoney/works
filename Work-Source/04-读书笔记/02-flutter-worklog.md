

###  2020年02月16日
-----------------------------------------------------------------



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

