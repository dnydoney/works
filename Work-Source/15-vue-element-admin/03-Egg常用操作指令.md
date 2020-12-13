###  2020年11月21日

-----------------------------------------------------------------


1、安装nodejs运行环境

nodejs版本必须≥8.0，建议使用LTS稳定版本
2、创建egg的环境

npm i egg-init -g  / cnpm i egg-init -g        //(仅需要安装一次)
3、创建项目

cd到项目目录中（注意：目录不要有中文、不要有空格）
 
egg-init egg-project --type=simple
 
cd egg-project
 
npm install
4、运行项目

npm run dev  
5、打开浏览器

地址栏输入：localhost:7001 / 127.0.0.1:7001 (默认端口号)




下面是部署操作


1.将egg项目除node_modules以外的文件压缩，使用xftp放入服务器并解压。我放在了/opt下

2.cd到解压的文件夹中，通过 npm install --production 安装项目依赖。

3. npm start 启动项目。

4.在前端将接口地址改为http://(服务器地址) ，这样就可以正常调用了

 



 ###  Egg.js环境搭建、创建及运行egg项目
-----------------------------------------------------------------
