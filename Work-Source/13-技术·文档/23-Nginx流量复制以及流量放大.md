# 技术·文档 |Nginx流量复制以及流量放大
-----------------------------------------------------------------

1. Nginx站点流量复制get及post请求


```
server {
        listen       80;
        server_name  web1.www.com;
        # 源站配置
        location / {
                access_log  /data/nginx/1.14.1/logs/web1/access.log  accesslog;
                mirror /mirror;
                mirror_request_body on;# Indicates whether the client request body is mirrored. default value is on.
                proxy_pass http://web1.upstream.name;
        }
        # 镜像站点配置
        location /mirror {
                internal; # 内部配置
                proxy_pass http://mirror.web1.upstream.name$request_uri;
                proxy_pass_request_body on; # Indicates whether the original request body is passed to the proxied server. default value is on
                proxy_set_header X-Original-URI $request_uri; # reset uri
        }
}


```
2. Nginx站点流量不允许复制post请求

```
server {
        listen       80;
        server_name  web1.www.com;

        # 源站配置
        location / {
                access_log  /data/nginx/1.14.1/logs/web1/access.log  accesslog;
                mirror /mirror;
                mirror_request_body off;# Indicates whether the client request body is mirrored. default value is on.
                proxy_pass http://web1.upstream.name;
        }

        # 镜像站点配置
        location /mirror {
                # 判断请求方法，不是GET返回403
                if ($request_method != GET) {
                    return 403;
                }
                internal; # 内部配置
                proxy_pass http://mirror.web1.upstream.name$request_uri;
                proxy_pass_request_body off; # Indicates whether the original request body is passed to the proxied server. default value is on
                proxy_set_header Content-Length ""; # mirror_request_body/proxy_pass_request_body都设置为off，则Conten-length需要设置为""，否则有坑
                proxy_set_header X-Original-URI $request_uri; # 使用真实的url重置url
        }
}


```
3. Nginx站点流量放大

```
server {
        listen       80;
        server_name  web1.www.com;
        # 源站配置
        location / {
                access_log  /data/nginx/1.14.1/logs/web1/access.log  accesslog;
                mirror /mirror;
                # 多加一份mirror，流量放大一倍
                mirror /mirror;
                mirror_request_body on;# Indicates whether the client request body is mirrored. default value is on.
                proxy_pass http://web1.upstream.name;
        }
        # 镜像站点配置
        location /mirror {
                internal; # 内部配置
                proxy_pass http://mirror.web1.upstream.name$request_uri;
                proxy_pass_request_body on; # Indicates whether the original request body is passed to the proxied server. default value is on
                proxy_set_header X-Original-URI $request_uri; # reset uri
        }
}
	
	
```

3. Nginx站点流量日志
```
server {
        listen       80;
        server_name  web1.www.com;

        # 源站配置
        location / {
                access_log  /data/nginx/1.14.1/logs/web1/access.log  accesslog;
                mirror /mirror;
                mirror_request_body off;# Indicates whether the client request body is mirrored. default value is on.
                proxy_pass http://web1.upstream.name;
        }

        # 镜像站点配置
        location /mirror {
                internal; # 内部配置
                # 跳转到下面的内部server
                proxy_pass http://127.0.0.1:10901$request_uri;
                proxy_pass_request_body off; # Indicates whether the original request body is passed to the proxied server. default value is on
                # Content-Length必须配置在mirror中否则无效
                proxy_set_header Content-Length ""; # mirror_request_body/proxy_pass_request_body都设置为off，则Conten-length需要设置为""，否则有坑
                proxy_set_header X-Original-URI $request_uri; # 使用真实的url重置url
        }
}

server {
    # server没法设置为内部
    listen 127.0.0.1:10901;
    location / {
        # 判断放在server，使得post请求日志可以记录
        if ($request_method != GET) {
            return 403;
        }
        access_log /data/nginx/1.14.1/logs/web1/access.log  accesslog;
        proxy_pass http://mirror.web1.upstream.name;
    }
}

```