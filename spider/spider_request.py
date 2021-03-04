# author:ToddCombs
from selenium import webdriver
import requests


# 这是一个假请求模拟程序，请配合spider_flask.py使用

url = 'http://127.0.0.1:5000/getInfo'


# 增加伪装headers后，浏览器识别可抓取数据
# headers = {
#     假装自己是浏览器
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#     把拿到的cookie拿过来
#     'Cookie': 'eda38d470a662ef3606390ac3b84b86f9; Hm_lvt_f1d3b035c559e31c390733e79e080736=1553503899; biihu__user_login=omvZVatKKSlcXbJGmXXew9BmqediJ4lzNoYGzLQjTR%2Fjw1wOz3o4lIacanmcNncX1PsRne5tXpE9r1sqrkdhAYQrugGVfaBICYp8BAQ7yBKnMpAwicq7pZgQ2pg38ZzFyEZVUvOvFHYj3cChZFEWqQ%3D%3D; Hm_lpvt_f1d3b035c559e31c390733e79e080736=1553505597',

# }


# 可以去这里clone免费代理ip的项目https://github.com/Python3WebSpider/ProxyPool
proxie = {
        'http': 'http://101.132.106.219:3129',
        'http': 'http://103.216.147.73:8080',

}
d = webdriver.Chrome()
d.get(url)

# session = requests.Session()
# d = session.get('https://biihu.cc/people/wistbean%E7%9C%9F%E7%89%B9%E4%B9%88%E5%B8%85', headers=headers)

# 伪装Headers信息后可以用该程序爬取spider_flask.py信息


if __name__ == '__main__':
    # 入参加入headers信息
    # d = requests.get(url, headers=headers)
    d = requests.get(url, proxies=proxie)
    print(d.text)
