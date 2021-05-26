# 技术·文档 |轻量级压测工具之Hey
-----------------------------------------------------------------

#下载hey
wget https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
#如果下载速度较慢，可使用xiaoz软件库链接
wget http://soft.xiaoz.org/linux/hey_linux_amd64
#赋予执行权限
chmod +x hey_linux_amd64
#移动文件到sbin目录
mv hey_linux_amd64 /usr/sbin/hey

如果是其它操作系统，请对号入座：

Linux 64-bit: https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
Mac 64-bit: https://hey-release.s3.us-east-2.amazonaws.com/hey_darwin_amd64
Windows 64-bit: https://hey-release.s3.us-east-2.amazonaws.com/hey_windows_amd64

举个例子：

hey -n 10000 -c 100 -m GET https://www.qq.com/
./hey_linux_amd64 -n 1000 -c 50 https://www.baidu.com/


-n：请求总数
-c：客户端连接数
-m：请求方法，比如GET/POST等
上面例子的含义就是对https://www.qq.com/发起100个GET并发请求，请求总数为10000个，执行完毕后hey还会打印统计信息，如下。

Summary:
  Total:        9.9769 secs
  Slowest:      0.3740 secs
  Fastest:      0.0350 secs
  Average:      0.0971 secs
  Requests/sec: 1002.3120

Response time histogram:
  0.035 [1]     |
  0.069 [894]   |■■■■■■
  0.103 [6193]  |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.137 [2158]  |■■■■■■■■■■■■■■
  0.171 [464]   |■■■
  0.205 [118]   |■
  0.238 [84]    |■
  0.272 [56]    |
  0.306 [29]    |
  0.340 [2]     |
  0.374 [1]     |

Latency distribution:
  10% in 0.0702 secs
  25% in 0.0802 secs
  50% in 0.0917 secs
  75% in 0.1056 secs
  90% in 0.1266 secs
  95% in 0.1510 secs
  99% in 0.2334 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0016 secs, 0.0350 secs, 0.3740 secs
  DNS-lookup:   0.0008 secs, 0.0000 secs, 0.1045 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0716 secs
  resp wait:    0.0896 secs, 0.0320 secs, 0.2326 secs
  resp read:    0.0054 secs, 0.0014 secs, 0.1429 secs

Status code distribution:
  [200] 10000 responses



  ```
  Usage: hey [options...] &lt;url&gt;
 
Options:
 
  # -n 指定运行的总请求数。默认值为200。
 
  -n  Number of requests to run. Default is 200.
 
 
  # -c 客户端并发执行的请求数，默认为50。总请求数不能小于并发数。
 
  -c  Number of workers to run concurrently. Total number of requests cannot
 
      be smaller than the concurrency level. Default is 50.
 
 
  # -q 客户端发送请求的速度限制，以每秒响应数QPS为单位，默认没有限制。
 
  -q  Rate limit, in queries per second (QPS) per worker. Default is no rate limit.
 
 
  # -z 发送请求的持续时长，超时后程序停止并退出。若指定了持续时间，则忽略总请求数(-n)，例如-z 10s，-z 3m
 
  -z  Duration of application to send requests. When duration is reached,
 
      application stops and exits. If duration is specified, n is ignored.
 
      Examples: -z 10s -z 3m.
 
 
  # -o 输出类型。若没有提供，则打印摘要。CSV是唯一支持的格式，结果以逗号分隔各个指标项。
 
  -o  Output type. If none provided, a summary is printed.
 
      "csv" is the only supported alternative. Dumps the response
 
      metrics in comma-separated values format.
 
 
  # -m 是HTTP方法，例GET，POST，PUT，DELETE，HEAD，OPTIONS方法
 
  -m  HTTP method, one of GET, POST, PUT, DELETE, HEAD, OPTIONS.
 
 
  # -H 代表HTTP请求头，可以用-H连续添加多个请求头。
 
  -H  Custom HTTP header. You can specify as many as needed by repeating the flag.
 
      For example, -H "Accept: text/html" -H "Content-Type: application/xml" .
 
 
  # -t 每个请求的超时时间（以秒为单位）。默认值为20s，数值0代表永不超时。
 
  -t  Timeout for each request in seconds. Default is 20, use 0 for infinite.
 
 
  # -A 代表HTTP响应头
 
  -A  HTTP Accept header.
 
 
  # -d代表HTTP请求正文
 
  -d  HTTP request body.
 
 
  # -D代表HTTP请求正文文件
 
  -D  HTTP request body from file. For example, /home/user/file.txt or ./file.txt.
 
 
  # -T内容类型，默认为“ text / html”。
 
  -T  Content-type, defaults to "text/html".
 
 
  # -a代表基本身份验证，用户名：密码。
 
  -a  Basic authentication, username:password.
 
 
  #-x代表 HTTP代理地址作, 使用host:port格式。
 
  -x  HTTP Proxy address as host:port.
 
 
  # -h2启用HTTP / 2
 
  -h2 Enable HTTP/2.
 
 
  # -host http主机头
 
  -host HTTP Host header.
 
 
  # -disable-compression 禁用压缩。
 
  -disable-compression  Disable compression.
 
  # -disable-keepalive禁用保持活动状态，防止重新使用不同的HTTP请求之间的TCP连接。
 
  -disable-keepalive    Disable keep-alive, prevents re-use of TCP
 
                        connections between different HTTP requests.
 
 
  # -disable-redirects 禁用HTTP重定向                     
 
  -disable-redirects    Disable following of HTTP redirects
 
  # -cpus 使用的cpu内核数。当前计算机的默认值为8核。
 
  -cpus                 Number of used cpu cores.
 
                        (default for current machine is 8 cores)
 
  
  ```


 ```
 
指定时长的get请求：客户端(-c)并发为2， 持续发送请求2s (-c)
 
hey -z 5s -c 2 https://www.baidu.com/
 
指定请求总数的get请求：运行2000次(-n)，客户端并发为50(-c)
 
hey -n 2000 -c 50  https://www.baidu.com/
 
指定host的get请求：使用的cpu核数为2 (-cpus), 压测时长为5s(-z), 并发数为2
 
hey -z 5s -c 2 -cpus 2 -host "baidu.com" https://220.181.38.148
 
请求带header的get接口：压测时长为5s (-z), 客户端发送请求的速度为128QPS, 请求头用-H添加
 
hey -z 5s -q 128 -H "client-ip:0.0.0.0" -H "X-Up-Calling-Line-Id:X.L.Xia" https://www.baidu.com/
 
post请求
 
hey -z 5s -c 50 -m POST -H "info:firstname=xiuli; familyname=xia" -d "year=2020&amp;month=1&amp;day=21" https://www.baidu.com/
 
代理模式，需额外配置proxy：因部分ip频繁发请求有风险，故可用-x设置白名单代理向服务器发请求
 
hey -z 5s -c 10 -x "http://127.0.0.1:8001" http://baidu.com/
 
shell for循环实现压测
 
for i in `seq 10`; do curl -v http://baidu.com; done
 
 ```

