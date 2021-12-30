# coding=utf-8
from urllib import request
import gzip
from io import StringIO
import configparser


def get_content(toUrl, count):
    """ Return the content of given url
        Args:
            toUrl: aim url
            count: index of this connect
        Return:
            content if success
            'Fail' if fail
    """

    cf = configparser.ConfigParser()
    cf.read("config.ini")
    cookie = cf.get("cookie", "cookie")

    headers = {
        'Cookie': cookie,
        'Host': 'www.zhihu.com',
        'Referer': 'http://www.zhihu.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept-Encoding': 'gzip'
    }

    req = request.urlopen(
        url=toUrl,
        headers=headers
    )

    try:
        opener = request.build_opener(request.ProxyHandler())
        request.install_opener(opener)

        page = request.urlopen(req, timeout=15)

        headers = page.info()
        content = page.read()
    except Exception as e:
        if count % 1 == 0:
            print(str(count) + ", Error: " + str(e) + " URL: " + toUrl)
        return "FAIL"

    if page.info().get('Content-Encoding') == 'gzip':
        data = StringIO.StringIO(content)
        gz = gzip.GzipFile(fileobj=data)
        content = gz.read()
        gz.close()

    return content
