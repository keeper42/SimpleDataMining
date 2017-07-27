#
# map(func, seq1[, seq2...])
# map()函数是将func作用于seq中的每一个元素， 
# 并用一个列表给出返回值，如果func为 None，作用同zip()。
#
def f(x):
	return x*x
res = map(f, range(10))
mres = list(res)
print("map:", mres)

#
# reduce(func, seq[, init])
# reduce函数即为化简，它是这样一个过程：
# 每次迭代，将上一次的迭代结果（第一次时为init的元素，
# 如没有init则为seq的第一个元素）与下一个元素一同执行一个二元的func函数。
#
from functools import reduce 
def add(x, y):
	return x+y
res = reduce(add, range(1, 10))
print("reduce:", res)

#
# filter(function or None, iterable)
# filter函数用于过滤序列中某些元素。和map、 reduce函
# 数一样， filter也接收一个函数和一个序列，不同的是，
# filter把传入的函数参数作用于序列中每一个元素，然后
# 根据返回值判断是true还是false来决定该元素是否被丢弃。
#
def is_odd(n):
	return n % 2 == 1
res = list(filter(is_odd, [1,2,3,5]))
print("filter:", res)

# 
# sorted(iterable, key=None, reverse=False)
# sorted()也是一个高阶函数，可以接收一个key函
# 数来实现自定义的排序。用sorted()排序的关键在
# 于实现一个映射函数。
# 
res = sorted([1, -3, -2, 4], key = abs)
print(res)

#
# 输入(input)输出(print)
#
print("{0} + {1} = {2}".format(1, 2, 3))

#
# handle = open(file, mode = 'r', encoding = None)
# file是文件名
# mode是文件操作的模式，有’w+’ ， ’a+’， ’r’ ， ’w’ 等等。
# encoding是文件的编码方式
# handle.close() 关闭文件
# file.cloed
# file.mode
# file.softspace
# file.write()
# file.read([count])
# file.seek(offset, [, from])
#
file = open("lx.txt", "w+")
file.write("2017\n")
file.seek(0, 0)    # 将指针定位到文件开头
print(file.read())
file.close()    # 刷新缓冲区里任何还没写入的信息

#
# python的os模块
# os.rename(current_file_name, new_file_name)
# os.remove(file)
# os.mkdir("newdir")
# os.chdir("newdir")
# os.getcwd()
# os.rmdir("dirname")
# 

#
# 进程通信
#
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程
def write(q):
	print("Process to write: $s" % os.getpid())
	for value in ["A", "B", "C"]:
		print("Put %s to queue..." % value)
		q.put(value)
		time.sleep(random.random())
# 读数据进程
def read(q):
	print("Process to read: %s" % os.getpid())
	while True:
		value = q.get(True)
		print("Get %s from queue." % value)
if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动子进程
	pw.start()
	pr.start()
	# 等待pw进程结束
	pw.join()
	# 强行终止pr进程
	pr.terminate()

# 
# 创建线程
# 
from threading import Thread

class MyThread(Thread):
	def __init__(self):
		Thread.__init__(self, name = "My Thread")

	def run(self):
		print("Hello, my name is %s" % self.getName())

process = MyThread()
process.start()

