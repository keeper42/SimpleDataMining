# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

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