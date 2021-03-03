# author:ToddCombs
from selenium import webdriver
import requests

# 这是一个假请求模拟程序，请配合spider_flask.py使用

url = 'http://127.0.0.1:5000/getInfo'
d = webdriver.Chrome()
d.get(url)

# 伪装Headers信息后可以用该程序爬取spider_flask.py信息


if __name__ == '__main__':
    d = requests.get(url)
    print(d.text)