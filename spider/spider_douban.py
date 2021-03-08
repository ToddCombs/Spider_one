# author:ToddCombs
import multiprocessing

from bs4 import BeautifulSoup
import requests
import xlwt
import time
import random


def request_douban(url):
    """请求db电影TOP250"""
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    try:
        response = requests.get(url, headers=head)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1

def save_to_excel(soup):
    """处理获取的数据存入excel中"""
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if(item.find(class_='inq')!=None):
            item_intr = item.find(class_='inq').string

        # print('抓电影：' + item_index + ' | ' + item_name +' | ' + item_img + ' | ' + item_score + ' | ' + item_author + ' | ' + item_intr )
        print('抓电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)

        n = n + 1


def main(page):
    """获取db评分排名前250部电影信息并存入excel中"""
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    html = request_douban(url)
    if html == None:
        print('get html None, page=' + str(page))
        return

    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


# def main(url):
#     """修改后多进程爬取db电影信息"""
#     html = request_douban(url)
#     soup = BeautifulSoup(html, 'lxml')
#     save_to_excel(soup)



if __name__ == '__main__':

    for i in range(0, 10):
            main(i)

    sec = random.random() % 5
    time.sleep(sec)

    book.save('C:\\Users\\Administrator\\PycharmProjects\\Spider_one\\spider\\static\\{}.xls'.format(u'豆瓣最受欢迎的250部电影'))

    # start = time.time()
    # urls = []
    # # 根据电脑CPU的内核数量创建相应的进程池，进程数不需要大于内核数，因为进程数创建的再多反而没好处
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # for i in range(0, 10):
    #     url = 'https://movie.douban.com/top250?start='+str(i * 25)+'&filter='
    #     urls.append(url)
    # # 通过map函数去执行主函数，将获得的url传过去
    # pool.map(main, urls)
    #
    # # 之后调用close方法，让它不在创建进程
    # pool.close()
    # # 调用join方法让进程池的进程执行完毕再结束
    # pool.join()

