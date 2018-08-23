#coding=utf-8
import logging
import os
import re
import time
from urllib.parse import urlparse  # py3
import pdfkit
import requests
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

class Crawler(object):
    """
    ������࣬�������涼Ӧ�ü̳д���
    """
    name = None

    def __init__(self, name, start_url):
        """
        ��ʼ��
        :param name: ��Ҫ������ΪPDF���ļ�����
        :param start_url: �������URL
        """
        self.name = name
        self.start_url = start_url
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.start_url))

    @staticmethod
    def request(url, **kwargs):
        """
        ��������,����response����
        :return:
        """
        response = requests.get(url, **kwargs)
        return response

    def parse_menu(self, response):
        """
        ��response�н���������Ŀ¼��URL����
        """
        raise NotImplementedError

    def parse_body(self, response):
        """
        ��������,������ʵ��
        :param response: ���淵�ص�response����
        :return: ���ؾ���������html�����ı�
        """
        raise NotImplementedError

    def run(self):
        start = time.time()
        print("Start!")
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        htmls = []
        count=1
        for index, url in enumerate(self.parse_menu(self.request(self.start_url))):
            html = self.parse_body(self.request(url))
            f_name = ".".join([str(index), "html"])
            with open(f_name, 'wb') as f:
                print("������ȡ�� %d ҳ......" % count)
                f.write(html)
                count += 1
            htmls.append(f_name)

        print("HTML�ļ�������ɣ���ʼת��PDF")
        pdfkit.from_file(htmls, self.name + ".pdf", options=options)
        print("PDFת����ɣ���ʼ�������HTML�ļ�")
        for html in htmls:
            os.remove(html)
        total_time = time.time() - start
        print(u"��ɣ��ܹ���ʱ��%f ��" % total_time)


class LiaoxuefengPythonCrawler(Crawler):
    """
    ��ѩ��Python3�̳�
    """
    def parse_menu(self, response):

        bsObj = BeautifulSoup(response.content, "html.parser")
        menu_tag = bsObj.find_all(class_="uk-nav uk-nav-side")[1]
        for li in menu_tag.find_all("li"):
            url = li.a.get("href")
            if not url.startswith("http"):
                url = "".join([self.domain, url])  # ��ȫΪȫ·��
            yield url

    def parse_body(self, response):
        try:
            bsObj = BeautifulSoup(response.content, 'html.parser')
            body = bsObj.find_all(class_="x-wiki-content")[0]

            # �������, ������ʾ
            title = bsObj.find('h4').get_text()
            center_tag = bsObj.new_tag("center")
            title_tag = bsObj.new_tag('h1')
            title_tag.string = title
            center_tag.insert(1, title_tag)
            body.insert(1, center_tag)

            html = str(body)
            # body�е�img��ǩ��src���·���ĸĳɾ���·��
            pattern = "(<img .*?src=\")(.*?)(\")"

            def func(m):
                if not m.group(2).startswith("http"):
                    rtn = "".join([m.group(1), self.domain, m.group(2), m.group(3)])
                    return rtn
                else:
                    return "".join([m.group(1), m.group(2), m.group(3)])

            html = re.compile(pattern).sub(func, html)
            html = html_template.format(content=html)
            html = html.encode("utf-8")
            return html
        except Exception as e:
            logging.error("��������", exc_info=True)


if __name__ == '__main__':
    start_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    crawler = LiaoxuefengPythonCrawler("��ѩ��Python�̳�", start_url)
    crawler.run()