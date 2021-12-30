# coding=utf-8
import requests
import http.cookiejar
from bs4 import BeautifulSoup
session = requests.Session()
session.cookies = http.cookiejar.LWPCookieJar("cookie")
agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.1.2.3000 Chrome/55.0.2883.75 Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Origin": "https://www.zhihu.com/",
    "Referer": "http://www.zhihu.com/",
    'User-Agent': agent
}

postdata = {
    'account': '825887013@qq.com',  # 填写帐号
    'password': 'zhihu@5426986',  # 填写密码
}
response = session.get("https://www.zhihu.com", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
postdata['_xsrf'] = xsrf
result = session.post('http://www.zhihu.com/login/email',
                      data=postdata, headers=headers)
session.cookies.save(ignore_discard=True, ignore_expires=True)



