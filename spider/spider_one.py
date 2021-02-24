# author:ToddCombs
import requests
import json
import re

def main(page):
    """抓取当当网前500本五星好评书籍并存入文件"""

    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
    html = request_dd(url)
    items = parese_result(html)

    for item in items:
        # 抓取成功写入文件
        write_item_to_file(item)


def request_dd(url):
    """抓取当当网500本书籍页面源代码"""
    try:
        response = requests.get(url)
        if response.status_code == 200:  # 判断页面返回码是否200，是则表示成功，之后返回页面代码
            return response.text
    except requests.RequestException:  # 否则返回异常
        return None


def parese_result(html):
    """处理抓取到的页面源代码"""
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }
    for item in items:
        print(item)

def write_item_to_file(item):
    """将处理好的数据写入文件"""
    print('开始写入数据 ==>' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()



if __name__ == "__main__":
   for i in range(1, 26):
       main(i)
