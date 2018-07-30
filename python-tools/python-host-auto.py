
#!/usr/bin/env python
#-*- coding: utf-8 -*-


import re
import urllib
import zipfile
import os, sys, stat
 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(html):
    reg = r'<a href="([^>]*?\.zip)"'
    aRe = re.compile(reg)
    allHref = aRe.findall(html)
    urllib.urlretrieve(allHref[0], 'd:\\myHosts.zip')  #第二个参数是下载后的hosts.zip存放路径，可以根据自己的需要进行更改
 
def unzipHosts():
    zfile = zipfile.ZipFile('d:\\myHosts.zip', 'r')
    for filename in zfile.namelist():
        data = zfile.read(filename)
        file = open('d:\\hosts', 'w+b') #参数1是解压后的文件的存放路径
        file.write(data)
        file.close()
 
def writeToFile(url):
    os.chmod(url, stat.S_IRWXU|stat.S_IRGRP) #由于系统hosts文件位于c盘系统目录下 所以需要更改文件权限 才能进行替换
    fromFile = open('D:\\hosts')
    data = fromFile.read();
    fromFile.close()
    toFile = open(url, 'w+b')
    toFile.write(data)
    toFile.close()
 

html = getHtml('http://www.gfsoso.org/1091/') 
getImg(html)
unzipHosts()
writeToFile('C:\\Windows\System32\drivers\etc\hosts')
