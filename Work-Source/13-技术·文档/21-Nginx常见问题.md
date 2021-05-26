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
2. Nginx站点代理转发后，文件上传，无法获取URL链接

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
3. Nginx站点 代理转发MQTT，部署小程序使用MQTT配置

```
server { 
	listen 443; 
	server_name mqtt.forwayapp.com;

	ssl on;
    ssl_certificate /www/ssl/3060252_mqtt.forwayapp.com.pem;
    ssl_certificate_key /www/ssl/3060252_mqtt.forwayapp.com.key;
	ssl_session_timeout 5m;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
	ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
	ssl_prefer_server_ciphers on;
	

	
    location / {
    	root   html; 
    	index  index.html index.htm;
	}
	
	# 监听mqtt
    location /mqtt {
		proxy_pass http://mqtt.forwayapp.com:8083;
		proxy_redirect off;
		proxy_set_header Host mqtt.forwayapp.com:8083;

        proxy_set_header Sec-WebSocket-Protocol mqtt;
    
    	# 这个是与你的 js客户端的库有关系，本博文的不需要，为了兼顾以后小伙伴，我这里注释了下！ 
    	#more_clear_headers Sec-WebSocket-Protocol;

    	# 这些都是 websocket必须要配置的
    	proxy_http_version 1.1;
    	proxy_set_header Upgrade $http_upgrade;
    	proxy_set_header Connection "upgrade";
	}
	
	
	server {
    listen 443;
    server_name www.domain.com; #填写绑定证书的域名
    
    ssl on;
    ssl_certificate certs/1_www.domain.com_bundle.crt;
    ssl_certificate_key certs/2_www.domain.com.key;
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #按照这个协议配置
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#按照这个套件配置
    ssl_prefer_server_ciphers on;

    location / {
        root   html; #站点目录
        index  index.html index.htm;
    }

    location = /mqtt {
        proxy_pass http://www.domain.com:8083;
        proxy_redirect off;
        proxy_set_header Host www.domain.com:8083;

        proxy_set_header Sec-WebSocket-Protocol mqtt;
        more_clear_headers Sec-WebSocket-Protocol;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        }
}

	
	
```