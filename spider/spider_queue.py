
import threading
import time
from queue import Queue


class CustomThread(threading.Thread):
    """
    我们还可以用一个叫做 Queue 的队列来创建线程池队列
    就是可以往里塞东西
    也可以往里拉东西
    所以我们在使用队列的时候
    最常用的方法就是 put 和 get 了
    我们创建一个长度为 6 的队列
    接着根据队列的长度创建了线程
    每个线程都让它们处于守护状态
    也就是需要的时候
    马上执行
    """
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue


    def run(self):
        while True:
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def moyu():
    """摸鱼开始"""
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def queue_pool():
    """队列池"""
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()

    for i in range(20):
        queue.put(moyu)
    queue.join()

if __name__ == '__main__':
    queue_pool()



