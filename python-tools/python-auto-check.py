# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://www.ccgp-shandong.gov.cn/sdgp2014/site/listsearchall.jsp?colcode=02&subject=%D7%CD%B2%A9%D6%B0%D2%B5%D1%A7%D4%BA&pdate=2018-08-14")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)
    print(html)