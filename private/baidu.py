# coding=utf-8
import requests
from bs4 import BeautifulSoup
import pymongo
import time
import datetime
import argparse
import platform
parser = argparse.ArgumentParser()
# 查取的tab类型
parser.add_argument('-t', '--tab')
args = parser.parse_args()
if(platform.system() == 'Windows'):
    dburl = 'mongodb://localhost:3001/'
if(platform.system() == 'Linux'):
    dburl = 'mongodb://{}:{}@{}:{}/?authSource={}'.format(
        "root", "5426986", "localhost", "27017", "admin")
myclient = pymongo.MongoClient(dburl)

meteorDB = myclient['hotnews']
collection = meteorDB['baidus']

# 热搜


def resou():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=realtime')
    soup = BeautifulSoup(res.text, 'html.parser')
    hots = soup.find_all(
        'div', {'class', 'category-wrap_iQLoo horizontal_1eKyQ'})
    for i in list(hots):
        obj = dict(img='', title='', content='', url='', hot='', type='hot')
        for j, child in enumerate(i):
            if j == 1:
                obj['url'] = child.get('href')
                obj['img'] = child.select('img')[0]['src']
            if j == 3:
                obj['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if j == 7:
                obj['title'] = child.select('.c-single-text-ellipsis')[0].text
                obj['content'] = child.select('.hot-desc_1m_jR')[0].text
        # print(obj, '\n')
        if collection.find_one({'type': obj['type'], 'title': obj['title']}) == None:
            obj['id'] = collection.estimated_document_count() + 1
            obj['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(obj)
            count = count + 1
    return count
# 小说


def novel():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=novel')
    soup = BeautifulSoup(res.text, 'html.parser')
    novels = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(novels):
        novel = dict(img='', title='', content='', url='',
                     hot='', type='novel', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                novel['img'] = child.select('img')[0]['src']
            if index == 3:
                novel['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                novel['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                novel['content'] = child.select('.desc_3CTjT')[0].text
                novel['author'] = child.select('.intro_1l0wp')[0].text
                novel['category'] = child.select('.intro_1l0wp')[1].text
                novel['url'] = child.select('.look-more_3oNWC')[0]['href']
        if collection.find_one({'type': novel['type'], 'title': novel['title']}) == None:
            novel['id'] = collection.estimated_document_count() + 1
            novel['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(novel)
            count = count + 1
    return count

# 电影


def moive():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=movie')
    soup = BeautifulSoup(res.text, 'html.parser')
    moives = soup.find_all('div', {'class': 'category-wrap_iQLoo'})

    for item in list(moives):
        moive = dict(img='', title='', content='', url='',
                     hot='', type='moive', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                moive['img'] = child.select('img')[0]['src']
            if index == 3:
                moive['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                moive['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                moive['content'] = child.select('.desc_3CTjT')[0].text
                moive['author'] = child.select('.intro_1l0wp')[1].text
                moive['category'] = child.select('.intro_1l0wp')[0].text
                moive['url'] = child.select('.look-more_3oNWC')[0]['href']
        # print(moive)
        if collection.find_one({'type': moive['type'], 'title': moive['title']}) == None:
            moive['id'] = collection.estimated_document_count() + 1
            moive['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(moive)
            count = count + 1
    return count

# 电视剧


def teleplay():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=teleplay')
    soup = BeautifulSoup(res.text, 'html.parser')
    teleplays = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(teleplays):
        teleplay = dict(img='', title='', content='', url='',
                        hot='', type='teleplay', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                teleplay['img'] = child.select('img')[0]['src']
            if index == 3:
                teleplay['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                teleplay['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                teleplay['content'] = child.select('.desc_3CTjT')[0].text
                teleplay['author'] = child.select('.intro_1l0wp')[1].text
                teleplay['category'] = child.select('.intro_1l0wp')[0].text
                teleplay['url'] = child.select('.look-more_3oNWC')[0]['href']
        # print(teleplay)
        if collection.find_one({'type': teleplay['type'], 'title': teleplay['title']}) == None:
            teleplay['id'] = collection.estimated_document_count() + 1
            teleplay['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(teleplay)
            count = count + 1
    return count

# 动漫


def cartoon():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=cartoon')
    soup = BeautifulSoup(res.text, 'html.parser')
    cartoons = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(cartoons):
        cartoon = dict(img='', title='', content='', url='',
                       hot='', type='cartoon', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                cartoon['img'] = child.select('img')[0]['src']
            if index == 3:
                cartoon['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                cartoon['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                cartoon['content'] = child.select('.desc_3CTjT')[0].text
                cartoon['category'] = child.select('.intro_1l0wp')[0].text
                cartoon['url'] = child.select('.look-more_3oNWC')[0]['href']
        # print(cartoon)
        if collection.find_one({'type': cartoon['type'], 'title': cartoon['title']}) == None:
            cartoon['id'] = collection.estimated_document_count() + 1
            cartoon['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(cartoon)
            count = count + 1
    return count

# 综艺


def variety():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=variety')
    soup = BeautifulSoup(res.text, 'html.parser')
    varietys = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(varietys):
        variety = dict(img='', title='', content='', url='',
                       hot='', type='variety', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                variety['img'] = child.select('img')[0]['src']
            if index == 3:
                variety['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                variety['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                variety['content'] = child.select('.desc_3CTjT')[0].text
                variety['category'] = child.select('.intro_1l0wp')[0].text
                variety['url'] = child.select('.look-more_3oNWC')[0]['href']
        # print(variety)
        if collection.find_one({'type': variety['type'], 'title': variety['title']}) == None:
            variety['id'] = collection.estimated_document_count() + 1
            variety['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(variety)
            count = count + 1
    return count

# 纪录片


def documentary():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=documentary')
    soup = BeautifulSoup(res.text, 'html.parser')
    documentarys = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(documentarys):
        documentary = dict(img='', title='', content='', url='',
                           hot='', type='documentary', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                documentary['img'] = child.select('img')[0]['src']
            if index == 3:
                documentary['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                documentary['title'] = child.select(
                    '.c-single-text-ellipsis')[0].text
                documentary['content'] = child.select('.desc_3CTjT')[0].text
                documentary['category'] = child.select('.intro_1l0wp')[0].text
                documentary['url'] = child.select(
                    '.look-more_3oNWC')[0]['href']
        # print(documentary)
        if collection.find_one({'type': documentary['type'], 'title': documentary['title']}) == None:
            documentary['id'] = collection.estimated_document_count() + 1
            documentary['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(documentary)
            count = count + 1
    return count
# 汽车


def car():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=car')
    soup = BeautifulSoup(res.text, 'html.parser')
    cars = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(cars):
        car = dict(img='', title='', content='', url='',
                   hot='', type='car', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                car['img'] = child.select('img')[0]['src']
                car['url'] = child.get('href')
            if index == 3:
                car['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                car['title'] = child.select('.c-single-text-ellipsis')[0].text
                car['content'] = child.select('.intro_1l0wp')[0].text
                car['category'] = child.select('.intro_1l0wp')[1].text

        # print(car)
        if collection.find_one({'type': car['type'], 'title': car['title']}) == None:
            car['id'] = collection.estimated_document_count() + 1
            car['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(car)
            count = count + 1
    return count

# 游戏


def game():
    count = 0
    res = requests.get('https://top.baidu.com/board?tab=game')
    soup = BeautifulSoup(res.text, 'html.parser')
    games = soup.find_all('div', {'class': 'category-wrap_iQLoo'})
    for item in list(games):
        game = dict(img='', title='', content='', url='',
                    hot='', type='game', author='', category='')
        for index, child in enumerate(item):
            if index == 1:
                game['img'] = child.select('img')[0]['src']
            if index == 3:
                game['hot'] = child.select('.hot-index_1Bl1a')[0].text
            if index == 7:
                game['title'] = child.select('.c-single-text-ellipsis')[0].text
                game['content'] = child.select('.desc_3CTjT')[0].text
                game['category'] = child.select('.intro_1l0wp')[0].text
                game['url'] = child.select('.look-more_3oNWC')[0]['href']
        # print(game)
        if collection.find_one({'type': game['type'], 'title': game['title']}) == None:
            game['id'] = collection.estimated_document_count() + 1
            game['create'] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            collection.insert_one(game)
            count = count + 1
    return count


if __name__ == '__main__':
    # print(args.tab)
    # if args.tab == '热搜':
    #     resou()
    # if args.tab == '小说':
    #     novel()
    # if args.tab == '电影':
    #     moive()
    # if args.tab == '电视剧':
    #     teleplay()
    # if args.tab == '动漫':
    #     cartoon()
    # if args.tab == '综艺':
    #     variety()
    # if args.tab == '纪录片':
    #     documentary()
    # if args.tab == '汽车':
    #     car()
    # if args.tab == '游戏':
    #     game()
    # if args.tab == 'all':
    r = resou()
    n = novel()
    m = moive()
    t = teleplay()
    c1 = cartoon()
    v = variety()
    d = documentary()
    c2 = car()
    g = game()
    print(datetime.datetime.now(), ':baidu \
        resou update {} item\
        novel update {} item\
        moive update {} item\
        teleplay update {} item\
        cartoon update {} item\
        variety update {} item\
        documentary update {} item\
        car update {} item\
        game update {} item'.format(r, n, m, t, c1, v, d, c2, g))
