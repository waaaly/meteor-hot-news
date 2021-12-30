# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas
import time
import requests
import re
import selenium

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches",["enable-logging"])
option.add_argument('ignore-certificate-errors')

class Spider():
    def __init__(self, url) -> None:
        self.url = url
        self.cur_page = 1
        self.web_source = []
        self.boot()

    def boot(self):
        self.chrome = webdriver.Chrome(
            executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe',options=option)
        self.chrome.start_client()

    def next_page(self):
        el_selector = "a.next.page-numbers"
        return self.chrome.find_elements(By.CSS_SELECTOR, el_selector)

    def click_el(self, el):
        self.chrome.execute_script("arguments[0].scrollIntoView(false);", el)
        time.sleep(1)
        self.chrome.execute_script("arguments[0].click();", el)
        self.cur_page += 1
        print('点击第', self.cur_page, '页')

    def crawl(self, total):
        self.chrome.get(self.url)
        print('开始访问目标网站。。。。')
        time.sleep(1)
        # while True:
        #     source = self.chrome.page_source
        #     self.web_source.append(source)
        #     time.sleep(3)

        #     next_el_list = self.next_page()
        #     if next_el_list == []:
        #         print('到达指定页数：', total,'关闭浏览器', '\n')
        #         self.chrome.quit()
        #         break
        #     else:
        #         self.click_el(next_el_list[0])
        #         print('正在加载第', self.cur_page, '页')
        #         time.sleep(3)

        for i in range(total):
            source = self.chrome.page_source
            self.web_source.append(source)
            time.sleep(3)
            print('第', len(self.web_source), '页追加成功')
            next_el_list = self.next_page()
            if (i+1 >= total) or (next_el_list == []):
                print('到达指定页数：', total,'关闭浏览器', '\n')
                self.chrome.quit()
                break
            else:
                self.click_el(next_el_list[0])
                print('正在加载第', self.cur_page, '页')
                time.sleep(3)


class Game():
    def __init__(self) -> None:
        # id
        self.id_selector = 'article.post'
        # 标题
        self.name_selector = 'h2.entry-title>a'
        # 主图
        self.img_selector = 'img.lazyloaded'
        # 标签
        self.tags_selector = 'span.meta-category'
        # 发布
        self.release_selector = 'time'
        # 浏览
        self.views_selector = 'li.meta-views'

    def setData(self, data_dict):
        return {
            'id': data_dict.id,
            'name': data_dict.name,
            'img': data_dict.img,
            'tags': data_dict.tags,
            'release': data_dict.release,
            'views': data_dict.views,
            'resources': data_dict.resources,
            'download_url': data_dict.download_url
        }


class Parser():
    def __init__(self, web_source) -> None:
        self.sources = web_source
        self.games = []

    def parser(self):
        print('开始抓取数据')
        ids = []
        names = []
        imgs = []
        tags = []
        releases = []
        views = []
        for html in self.sources:
            soup = BeautifulSoup(html, 'html.parser')
            ids = ids + soup.select(Game().id_selector)
            names = names + soup.select(Game().name_selector)
            imgs = imgs + soup.select(Game().img_selector)
            tags = tags + soup.select(Game().tags_selector)
            releases = releases + soup.select(Game().release_selector)
            views = views + soup.select(Game().views_selector)
        
        # print( '\n'.join(['%s:%s' % item for item in game.__dict__.items()]))
        for index in range(len(names)):
            game = Game()
            print('总计个数：', len(names))
            print('正在处理:', index+1, names[index].text)
            print('当前进度: {:.2%}'.format((index+1)/len(names)), '\n')
            game.id = ids[index].get('id').replace('post-', '')
            game.name = names[index].text
            game.img = imgs[index].get('src')
            game.tags = tags[index].text
            game.views = views[index].text
            game.release = releases[index].get('datetime')
            # 访问 id 地址看是否有资源下载
            if self.has_releases(game.id):
                down_url = self.get_downland_url(game.id)
                game.resources = self.get_downland_text(down_url)
                game.download_url = down_url
            else:
                game.resources = ''
                game.download_url = ''
            self.games.append(game)

    def has_releases(self, game_id):
        res = requests.get(url='https://switch520.com/' +
                           str(game_id) + '.html')
        soup = BeautifulSoup(res.text, 'html.parser')
        target = soup.find_all('div', id='cao_widget_pay-4')
        if list(target) == []:
            return False
        else:
            return True

    def get_downland_url(self, game_id):
        res = requests.get(
            url="https://switch520.com/go?post_id="+str(game_id))
        soup = BeautifulSoup(res.text, 'html.parser')
        urls = re.findall(r"'(.*?)'", soup.script.text, re.DOTALL)
        return urls[0]

    def get_downland_text(self, url):
        res = requests.get(url=url)
        soup = BeautifulSoup(res.text, 'html.parser')
        divs = soup.find_all('div', {'class': 'entry-content'})
        if list(divs) == []:
            return ''
        else:
            return list(divs)[0].text.strip('/n')

    def parse_game(self):
        return [Game().setData(i) for i in self.games]


start = time.time()

target_url = 'https://switch520.com/'
s = Spider(target_url)
s.crawl(10)

p = Parser(s.web_source)
p.parser()

g = pandas.DataFrame(p.parse_game())
print('正在写入文件..')
g.to_csv('./games.csv', index=False, mode='w', encoding='utf-8-sig')

end = time.time()
m, s = divmod(end-start, 60)
h, m = divmod(m, 60)
print ("总计耗时：%02d:%02d:%02d" % (h, m, s))
# url = "https://switch520.com/wp-admin/admin-ajax.php"
# data = {"action":"user_down_ajax","post_id":"24831"}
# res = requests.post(url=url,data=data)
# print(res.text)


# res = requests.get(url='https://switch520.com/' + str(18246) + '.html')
# soup = BeautifulSoup(res.text, 'html.parser')
# target = soup.find_all('div', id='cao_widget_pay-4')
# print(list(target))

# res = requests.get(url='https://switch520.net/1363.html')
# soup = BeautifulSoup(res.text, 'html.parser')
# text = soup.find_all('div',{'class':'entry-content'})
# print(list(text)[0].text)
