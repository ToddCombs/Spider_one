# author:ToddCombs
from multiprocessing import Process
# 使用multiprocessing实现多进程，用Process类创建进程
from multiprocessing import Pool
# 使用进程池的方式


# def f(name):
#     print('hello', name)
def f(x):
    return x*x


if __name__ == '__main__':
    # p = Process(target=f, args=('ToddCombs',))
    # p.start()
    # # p.join()
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

