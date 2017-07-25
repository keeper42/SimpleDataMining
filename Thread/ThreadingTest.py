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