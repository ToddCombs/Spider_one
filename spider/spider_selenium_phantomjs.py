# author:ToddCombs
# 目前由于firefox，chrome等主流浏览器已推出无头模式，phantomjs已停更。
# 这里仅抓取数据使用该方法
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

# b = webdriver.PhantomJS()
b = webdriver.Chrome()
WAIT = WebDriverWait(b, 10)
b.set_window_size(1400, 900)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('蔡徐坤篮球', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕数')
sheet.write(0, 5, '发布时间')

n = 1

def search():
    """查询B站上的蔡徐坤篮球视频"""
    try:
        print('开始访问B站。。。')
        b.get('http://www.bilibili.com/')

        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_searchform > input')))
        submit = WAIT.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button')))

        input.send_keys('蔡徐坤 篮球')
        submit.click()

        print('跳转到新窗口')
        all_h = b.window_handles
        b.switch_to.window(all_h[1])
        get_source()

        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           "#all-list > div.flow-loader > div.page-wrap > dir > ul > li.page-item.last > button")))
        return int(total.text)
    except TimeoutException:
        return search()


def next_page(page_num):
    """获取页面号，下一页数据"""
    try:
        print('获取下一页数据')
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#all-list > div.flow-loader > dir.page-wrap > dir > ul > li.page-item.active > button'),
                                                         str(page_num)))
        get_source()
    except TimeoutException:
        b.refresh()
        return next_page(page_num)



def get_source():
    """获取页面资源"""
    pass

