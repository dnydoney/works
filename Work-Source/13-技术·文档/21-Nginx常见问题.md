# 技术·文档 |Nginx常见问题
-----------------------------------------------------------------

1. Nginx站点刷新显示404错误

```
  location / {
       root   html;
       index  index.html index.htm;
	   try_files $uri $uri/ /index.html;
  }

```
1. Nginx站点代理转发后，文件上传，无法获取URL链接

```
   location / {
	     #node.js应用的端口
             proxy_pass http://127.0.0.1:96;
             root anki;
             #proxy_set_header Host $http_host;
	     proxy_redirect off;
	     proxy_set_header Host $http_host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }    

```