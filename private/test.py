# coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd   # 为了存储到csv
 
 
class Spider():
    def __init__(self,target_url):
        self.url = target_url
        self.raw_pages = []
        self.boot()
 
    def boot(self):
        self.chrome = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.chrome.start_client()
 
    def crawl(self):
        self.chrome.get(self.url)
        print('loading Webpage...')
        time.sleep(5)
        while True:
            raw_page = self.chrome.page_source
            self.raw_pages.append(raw_page)
            time.sleep(2)
            if self.next_page():
                next_page_ele = self.next_page()[0]
                self.click_ele(next_page_ele)
                print('点击后加载页面...')
                time.sleep(5)
            else:
                break
 
    def click_ele(self,ele):
        self.chrome.execute_script("arguments[0].scrollIntoView(false);", ele)  # 移动到元素element对象的“底端”，与当前窗口的“底部”对齐
        time.sleep(2)
        self.chrome.execute_script("arguments[0].click();", ele)  # 不管元素有没有被遮挡，直接在元素上发送单击
        print('点击下一页')
 
    def next_page(self):
        sel = 'span[class="pager_next "]'    # 可点的"下一页"的元素，不同于灰的“下一页”元素
        return self.chrome.find_elements_by_css_selector(sel)  # 返回一个列表
 
class Parser():
    def __init__(self,raw_pages):
        self.raw_pages = raw_pages
        self.jobs = []
        pass
 
    def parse(self):
        for html in self.raw_pages:
            soup = BeautifulSoup(html,'html.parser')
            pos_sel = 'div.position h3'   # text
            time_sel = 'span.format-time'   # text
            money_sel = 'span.money'  # text
            company_sel = 'div.company_name>a'   # text
            link_sel = 'a.position_link'  # href
 
            pos_eles = soup.select(pos_sel)
            time_eles = soup.select(time_sel)
            money_eles = soup.select(money_sel)
            company_eles = soup.select(company_sel)
            link_eles = soup.select(link_sel)
 
            for p,t,m,c,l in zip(pos_eles,time_eles,money_eles,company_eles,link_eles):
                cell = {
                    'position':p.text,
                    'time':t.text,
                    'money':m.text,
                    'company':c.text,
                    'link':l.get('href')
                }
                #print(cell)
                self.jobs.append(cell)
 
    def get_jobs(self):
        return [Job(j) for j in self.jobs]
 
class Job():
    def __init__(self,data_dict):
        self.position = data_dict.get('position')  # dict.get('key')优于 dict['key']，可以不报错
        self.time = data_dict.get('time')
        self.money = data_dict.get('money')
        self.company = data_dict.get('company')
        self.link = data_dict.get('link')
 
    def is_today(self):
        return ':' in self.time
 
 
target_url = 'https://www.lagou.com/jobs/list_python/p-city_2?px=default&district=朝阳区#filterBox'
s = Spider(target_url)
s.crawl()
print('s.raw_pages的页数：',len(s.raw_pages))
p = Parser(s.raw_pages)
p.parse()
print('-'*40)
jobs = p.get_jobs()
num = 0
for job in jobs:
    if job.is_today():
        num += 1
        print(num,job.position,job.time, job.company)
 
jobs_df = pd.DataFrame(p.jobs)
jobs_df.to_csv('./lagouwang.csv', index=False, mode='w',encoding='utf-8-sig')