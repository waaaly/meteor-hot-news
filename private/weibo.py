# coding=utf-8
import requests
from bs4 import BeautifulSoup
import datetime
import time
import re
import pymongo
from io import BytesIO
import gzip
import zlib
import argparse
import platform
parser = argparse.ArgumentParser()
# 查取的tab类型
parser.add_argument('-t', '--tab')
args = parser.parse_args()
cookies = dict(SUB='_2AkMWyoFgf8NxqwJRmf8Sz2vjbI12ywnEieKglnC7JRMxHRl-yT9jqkc5tRB6PUqvgz6jjf3-BTmnG1Ly84wS--FZv_e0',
               SUBP='0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5MXpVwGGyBB5_-nI_mxSfD')
"""
热搜：https://s.weibo.com/top/summary   wbHots
要问 https://s.weibo.com/top/summary?cate=socialevent   wbYaoWen
文娱 https://s.weibo.com/top/summary?cate=entrank wbWenYu
"""
if(platform.system() == 'Windows'):
    dburl = 'mongodb://localhost:3001/'
if(platform.system() == 'Linux'):
    dburl = 'mongodb://{}:{}@{}:{}/?authSource={}'.format("root","5426986","localhost","27017","admin")
myclient = pymongo.MongoClient(dburl)
meteorDB = myclient['hotnews']
qColltion = meteorDB['weibos']


def parser(data):
    count = 0
    res = requests.get(data['url'], cookies=cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    td02 = soup.find_all('td', {'class': 'td-02'})
    for td in td02:
        a = list(td.children)[1]
        obj = dict(id=0, url='', title=a.text, hot='', type=data['type'])
        # print(a.text)
        for i, j in enumerate(list(td.children)):
            if i == 3:
                obj['hot'] = j.text
        url = "https://s.weibo.com/" + a.get('href')
        obj['url'] = url
        if qColltion.find_one({"title": obj['title']}) == None:
            obj['id'] = qColltion.estimated_document_count() + 1

            obj['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            qColltion.insert(obj)
            count = count + 1
    return count

if __name__ == '__main__':
    total = 0
    for i in [
        {
            'type': 'hot',
            'url': 'https://s.weibo.com/top/summary',
        },
        {
            'type': 'yaowen',
            'url': 'https://s.weibo.com/top/summary?cate=socialevent',
        },
        {
            'type': 'wenyu',
            'url': 'https://s.weibo.com/top/summary?cate=entrank'
        },
    ]:
        total = total + parser(i)

    print(datetime.datetime.now(), ': weibo udpate total {} item!'.format(total))
