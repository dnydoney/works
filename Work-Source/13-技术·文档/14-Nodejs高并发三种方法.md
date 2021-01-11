# 技术·文档 | Nodejs高并发三种方法
-----------------------------------------------------------------

1、 安装环境： Centos7，Mysql5.7

2、用eventproxy实现控制并发

```   
    var EventProxy = require('eventproxy');

    const most = 5;//并发数5
    var urllist = [....];//待抓取url列表，100个

    function foo(start){
        var ep = new EventProxy();
        ep.after('ok',most,function(){
            foo(start+most);//一个批次任务完成，递归进行下一批任务
        });
        var q=0;
        for(var i=start;i<urllist.length;i++){
            if(q>=most){
                break;//最多添加most个任务
            }
            http.get(urllist[i],function(res){
                //....
                res.on('end',function(){
                    ep.emit('ok');//一个任务完成，触发一次ok事件
                });
            });
            q++;
        }
    }
    foo(0);

```

3、async.mapLimit 控制并发
```
	var async = require('async');

    //模拟一组连接地址
    var urls = [];
    for(var i = 0; i < 30; i++) {
        urls.push('http://datasource_' + i);
    }
    console.log(urls);

    // 并发连接数的计数器
    var concurrencyCount = 0;

    // 并发抓取数据的过程
    var fetchUrl = function (url, callback) {
        // delay 的值在 2000 以内，是个随机的整数
        var delay = parseInt((Math.random() * 10000000) % 2000, 10);
        concurrencyCount++;
        console.log('现在的并发数是', concurrencyCount, '，正在抓取的是', url, '，耗时' + delay + '毫秒');
        setTimeout(function () {
            concurrencyCount--;
            //抓取成功，调用回调函数
            callback(null, url + ' html content');
        }, delay);
    };

    //使用 async.mapLimit 来 5 个并发抓取，并获取结果
    async.mapLimit(urls, 5, function (url, callback) {
        fetchUrl(url, callback);
    }, function (err, result) {
        //所有连接抓取成功，返回回调结果列表
        console.log('final:');
        console.log(result);
    });



```

4、使用async.queue 控制并发
```
    "use strict"
    var http = require('http');
    var cheerio = require('cheerio');
    var URL = require('url');
    var path = require('path');
    var fs = require('fs');
    var async = require('async');

    var baseUrl = "http://cnodejs.org/";
    var targetUrl = "http://cnodejs.org/";
    var stime = new Date();

    function sGet(url,callback){
      var chunks = [];
      http.get(url,(res)=>{
        if (res.statusCode != '200') {
          callback({message:"抓取失败,状态码:"+res.statusCode,url:url});
          return;
        }
        res.on('data',(chunk)=>{
          chunks.push(chunk);
        });
        res.on('end',()=>{
          callback(null,Buffer.concat(chunks).toString());
        });
      }).on('error',(e)=>{
        callback({message:"抓取失败",url:url,err:e});
      });
    }

    sGet(targetUrl,(err,data)=>{
      if (err) {
        console.log(err);
        return false;
      }
      var $ = cheerio.load(data);
      var anchors = $("#topic_list a.topic_title");
      console.log('共'+anchors.length+'个任务');

      const most=5;//并发数
        //创建队列并指定并发数
      var q=async.queue(function(url,callback){
        var filename = path.basename(url)+'.txt';
        sGet(url, (err, data)=> {
          if (err) {
            callback(err);
            return false;
          }
          fs.writeFile('./html/' + filename, data, function (err) {
            if (err) {
              throw err;
            }
            callback(null,filename);
          });
        });
      },most);

      q.drain = function() {
        console.log('任务全部完成,共耗时:'+(new Date()-stime)+'ms');
      }

      anchors.each(function(){
        var url = URL.resolve(baseUrl,$(this).attr('href'));
        q.push(url,function(err,filename){
          if (err) {
            console.log(err);
            return;
          }
          console.log("finished:"+filename);
        });
      });
    });


```