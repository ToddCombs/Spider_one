
import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor


def moyu_time(name, delay, counter):
    """每隔一秒钟获取一次数据"""
    while counter:
        time.sleep(delay)
        print("%s 开始摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


class MyThread(threading.Thread):
    """创建一个线程子类"""
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 10)
        print("退出线程：" + self.name)


# # 创建线程，toddcombs找了两个人来摸鱼，让小明摸一次休息1秒，让小红摸一次休息2秒
# thread_one = MyThread(1, "小明", 1)
# thread_two = MyThread(2, "小红", 2)
#
# # 开启新线程
# thread_one.start()
# thread_two.start()
#
# # 等待线程中止
# thread_one.join()
# thread_two.join()
# print("退出主线程")


if __name__ == '__main__':
    # moyu_time('toddcombs', 1, 20)
    # 线程池内设置20个线程，循环每次拿一个线程摸鱼，不用重复创建销毁线程
    pool = ThreadPoolExecutor(20)
    for i in range(1, 5):
        pool.submit(moyu_time('toddcombs' + str(i),1 ,3))
