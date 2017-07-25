# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

from multiprocessing import Process, Queue, Manager, Pool

# compute train_loss and do something
def worker(q, i, num):
	train_loss = q.get()
	for j in range(i, i + 40):
		loss = getLoss()
	train_loss += loss
	q.put(train_loss)

# create processes
q = Queue()
jobs = []
for i in range(1, 2000, 40):    # the interval is 40
	p = Process(target = worker, args = (q, i, 40))
	p.start()
	jobs.append(p)
for p in jobs:
	p.join()

q.get()