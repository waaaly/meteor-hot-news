# coding=utf-8
import requests
from bs4 import BeautifulSoup
import pymongo
import time
import datetime
import argparse
import platform
# if(platform.system() == 'Windows'):
#     dburl = 'mongodb://localhost:3001/'
# if(platform.system() == 'Linux'):
dburl = 'mongodb://{}:{}@{}:{}/hotnews?authSource={}'.format(
    "hotnews", "5426986", "1.12.246.138", "27017", "admin")
myclient = pymongo.MongoClient(dburl)
meteorDB = myclient['hotnews']
collection = meteorDB['doubans']

headers = {'referer': 'http://jandan.net/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}


def movie():
    count = 0
    # driver.get('https://movie.douban.com/')
    res = requests.get('https://movie.douban.com/', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    moives = soup.find_all('li', {'class': 'ui-slide-item'})
    # print(list(moives))
    """
    演员
    评分 span subject-rate
    """

    for index, item in enumerate(list(moives)):
        movie = dict(id=0, title='', release='', region='', actors='',
                     director='', duration='', rate='', rater='',
                     img='', url='', type='movie')
        if item.select('.ticket_btn') != []:
            movie['actors'] = item['data-actors']
            movie['director'] = item['data-director']
            movie['duration'] = item['data-duration']
            movie['rate'] = item['data-rate']
            movie['rater'] = item['data-rater']
            movie['region'] = item['data-region']
            movie['release'] = item['data-release']
            movie['title'] = item['data-title']
            movie['img'] = item.select('img')[0]['src']
            movie['url'] = item.select('a')[0]['href']

            if collection.find_one({'type': movie['type'], 'title': movie['title']}) == None:
                movie['id'] = collection.estimated_document_count() + 1
                movie['create'] = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime())
                collection.insert_one(movie)
                count = count + 1
    return count


def book():
    count = 0
    res = requests.get(
        'https://book.douban.com/chart?subcat=all&icn=index-topchart-popular', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    books = soup.find_all('li', {'class': 'clearfix'})
    for item in list(books):
        book = dict(id=0, title='', release='', region='', actors='',
                    director='', duration='', rate='', rater='',
                    img='', url='', type='book')
        book['title'] = item.select('.fleft')[1].text
        book['actors'] = item.select('.subject-abstract')[0].text
        book['url'] = item.select('a')[0]['href']
        book['img'] = item.select('img')[0]['src']
        book['rate'] = item.select('span')[1].text
        book['rater'] = item.select('span')[2].text

        if collection.find_one({'type': book['type'], 'title': book['title']}) == None:
            book['id'] = collection.estimated_document_count() + 1
            book['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(book)
            count = count + 1
    return count


def music():
    count = 0
    res = requests.get('https://music.douban.com/chart', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    musics = list(soup.find_all('li', {'class': 'clearfix'}))
    for i in range(10):
        music = dict(id=0, title='', release='', region='', actors='',
                     director='', duration='', rate='', rater='',
                     img='', url='', type='music')
        music['url'] = musics[i].select('a')[0]['href']
        music['img'] = musics[i].select('img')[0]['src']
        music['release'] = musics[i].select('.days')[0].text
        intro = musics[i].select('.intro')[0]
        music['title'] = intro.select('a')[0].text
        music['actors'] = intro.select('p')[0].text

        if collection.find_one({'type': music['type'], 'title': music['title']}) == None:
            music['id'] = collection.estimated_document_count() + 1
            music['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(music)
            count = count + 1
    return count


def group(start):
    count = 0
    res = requests.get(
        'https://www.douban.com/group/explore'+start, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    explores = list(soup.find_all('div', {'class': 'channel-item'}))
    for item in list(explores):
        explore = dict(id=0, title='', release='', region='', actors='',
                       director='', duration='', rate='', rater='',
                       img='', url='', type='group', content='', gUrl='')
        explore['rater'] = item.select('.likes')[0].text
        explore['url'] = item.select('a')[0]['href']
        explore['title'] = item.select('a')[0].text
        explore['gUrl'] = item.select('span')[0].select('a')[0]['href']
        explore['actors'] = item.select('span')[0].select('a')[0].text
        explore['release'] = item.select('span')[1].text

        if item.select('.pic-wrap') != []:
            explore['img'] = item.select(
                '.pic-wrap')[0].select('img')[0]['src']
        if item.select('p') != []:
            explore['content'] = item.select('p')[0].text

        if collection.find_one({'type': explore['type'], 'title': explore['title']}) == None:
            explore['id'] = collection.estimated_document_count() + 1
            explore['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(explore)
            count = count + 1
    return count


if __name__ == '__main__':
    m = movie()
    b = book()
    m2 = music()
    g = group('')
    print(datetime.datetime.now(), ':douban \
    movie update {} item\
    book update {} item\
    music update {} item\
    group update {} item'.format(m, b, m2,  g))

    # for i in range(458):
    #     start = '?start=' + str(i*30)
    #     count = group(start)
    #     print(i+1, ':', count, 'item')
