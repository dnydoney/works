import urllib.request


class HtmlDownloader(object):
    def download(self, chaper_url):
        if chaper_url is None:
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=chaper_url, headers=headers)
        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            return None

        return response.read()
