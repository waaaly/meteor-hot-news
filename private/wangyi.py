# coding=utf-8
import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymongo
from selenium.webdriver.common.by import By
from selenium import webdriver
import platform
option = webdriver.ChromeOptions()
#静默模式
# option.add_argument('headless')
option.add_experimental_option("excludeSwitches",["enable-logging"])
option.add_argument('ignore-certificate-errors')
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

if(platform.system()=='Windows'):
    dburl = 'mongodb://localhost:3001/'
if(platform.system()=='Linux'):
    dburl = 'mongodb://{}:{}@{}:{}/?authSource={}'.format("root","5426986","localhost","27017","admin")
myclient = pymongo.MongoClient(dburl)
collection = myclient['hotnews']['wangyis']

def chrome():
    browser = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=option)
    browser.start_client()
    browser.get('https://www.163.com/special/007797UO/index_a11y.html')
    btn_els = browser.find_elements(by=By.CSS_SELECTOR,value="button.header_nav_item")
    for i,btn in enumerate(list(btn_els)):
        print(i,btn.text)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        news = soup.find_all('li',{'class':'news'})
        for new in list(news):
            item = {'id':'','type':btn.text,'title':'','url':'','create':''}
            item['title'] = new.text
            item['url'] = new.select('a')[0]['href']
            if collection.find_one({'title':item['title']}) == None:
                item['id'] = collection.estimated_document_count() + 1 
                item['create'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                collection.insert_one(item)
        if i+1 < len(list(btn_els)):
            list(btn_els)[i+1].click()
            time.sleep(2)

    browser.quit()
def start():
    res = requests.get('https://www.163.com/special/007797UO/index_a11y.html')
    soup = BeautifulSoup(res.text,'html.parser')
    divs = soup.find_all('div',{'class':'main_panel'})
    update = dict({
        '0':0,'1':0,'2':0,
        '3':0,'4':0,'5':0,
        '6':0,'7':0,'8':0,
    })
    for i,div in enumerate(list(divs)):
        news = div.select('li')
        for li in list(news):
            type = (i == 0 and 'news') or (i == 1 and 'tiyu') \
                or (i == 2 and 'yule') or (i == 3 and 'caijing') \
                or (i == 4 and 'qiche') or (i == 5 and 'keji') \
                or (i == 6 and 'jiaju') or (i == 7 and 'shishang') \
                or (i == 8 and 'fangchan') 
            item = {'id':'','type':type,'title':'','url':'','create':''}
            item['title'] = li.text
            item['url'] = li.select('a')[0]['href']
            if collection.find_one({'title':item['title']}) == None:
                item['id'] = collection.estimated_document_count() + 1 
                item['create'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                collection.insert_one(item)
                update[str(i)] = update[str(i)] + 1
    return update
if __name__ == '__main__':
    update = start()
    print(datetime.datetime.now(), ':wangyi \
    yaowen update {} item\
    tiyu update {} item\
    yule update {} item\
    caijing update {} item\
    qiche update {} item\
    keji update {} item\
    jiaju update {} item\
    shishang update {} item\
    fangchan update {} item'.format(\
        update['0'],update['1'],update['2'],\
        update['3'],update['4'],update['5'],\
        update['6'],update['7'],update['8'],))