
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
    urllib.urlretrieve(allHref[0], 'd:\\myHosts.zip')  #�ڶ������������غ��hosts.zip���·�������Ը����Լ�����Ҫ���и���
 
def unzipHosts():
    zfile = zipfile.ZipFile('d:\\myHosts.zip', 'r')
    for filename in zfile.namelist():
        data = zfile.read(filename)
        file = open('d:\\hosts', 'w+b') #����1�ǽ�ѹ����ļ��Ĵ��·��
        file.write(data)
        file.close()
 
def writeToFile(url):
    os.chmod(url, stat.S_IRWXU|stat.S_IRGRP) #����ϵͳhosts�ļ�λ��c��ϵͳĿ¼�� ������Ҫ�����ļ�Ȩ�� ���ܽ����滻
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
