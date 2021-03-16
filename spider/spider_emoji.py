# author:ToddCombs
import os
from time import time
import requests
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread


class DownloadeEmoji(Thread):

    def __init__(self, queue, path):
        """爬取表情包存储到"""
        Thread.__init__(self)
        self.queue = queue
        self.path = '/static/'
        if not os.path.exists(path):
            os.makedirs(path)

    def run(self):
        while True:
            url = self.queue.get()
            try:
                download_emoji(url, self.path)
            finally:
                self.queue.task_done()


def download_emoji(url, path):
    """下载表情包"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    emoji_list = soup.find_all('emoji', class_='ui image lazy')

    for emoji in emoji_list:
        image = emoji.get('data-original')
        title = emoji.get('title')
        print('下载图片： ', title)

        try:
            with open(path + title + os.path.splitext(image)[-1], 'wb') as f:
                emoji = requests.get(image).content
                f.write(emoji)
        except OSError:
            print('length failed')
            break

if __name__ == '__main__':

    start = time()

    # 构建所有链接
    _url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [_url.format(page=page) for page in range(1, 4328+1)]

    queue = Queue()
    path = '/static/'

    # 创建线程
    for x in range(10):
        worker = DownloadeEmoji(queue, path)
        worker.daemon = True
        worker.start()

    # 加入队列
    for url in urls:
        queue.put(url)

    queue.join()

    print('下载完毕耗时： ' + time()-start)






