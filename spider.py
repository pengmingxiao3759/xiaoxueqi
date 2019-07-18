from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://piyao.sina.cn/")
time.sleep(1)

for i in range(0,30):#模拟滚轮下拉，生成页面，平均每次生成3天的新闻
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(0.5) 


titles = driver.find_elements_by_xpath("//div[@class='left_title']")
data=driver.find_elements_by_xpath("//div[@class='comment_text']")
title=[]
da=[]
for a in titles:
    title.append(a.text)
for b in data:
    da.append(int(b.text))
title_and_data=zip(title,da)
high=sorted(title_and_data,key=lambda x:x[1])
print("本季最热门:\t")
for a in high[-1:-11:-1]:
    print(a[0],'\t',"评论数:",a[1],'\n')