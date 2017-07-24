#
# 生产者类
#

import time, random
from threading import Thread, currentThread

# class SharedCell(object):
#     """Shared data for the producer/consumer problem."""
#     def __init__(self):
#         self._data = -1

#     def setData(self, data):
#         """Producer's method to write shared data."""
#         print("%s setting data to %d" % \
#              (currentThread().getName(), data))
#         self._data = data
    
#     def getData(self):
#         """Consumer's method to read from shared data."""
#         print("%s accessing data %d" % \
#              (currentThread().getName(), self._data))
#         return self._data

# 加锁
class SharedCell(object):
    """Shared data for the producer/consumer problem."""
    def __init__(self):
        self._data = -1
        self.__writable = True
        self.__condition = Condition()
        
    def setData(self, data):
        """Producer's method to write shared data."""
        self.__condition.acquire()
        while not self.__writable:
            self.__condition.wait()
        print("%s setting data to %d" % \
             (currentThread().getName(), data))
        self._data = data
        self.__writable = False
        self.__condition.notify()
        self.__condition.release()
    
    def getData(self):
        """Consumer's method to read from shared data."""
        self.__condition.acquire()
        while self.__writable:
            self.__condition.wait()
        print("%s accessing data %d" % \
             (currentThread().getName(), self._data))
        self.__writable = True
        self.__condition.notify()
        self.__condition.release()
        return self._data

class Producer(Thread):
    """Represents a producer."""
    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self.__cell = cell
        self.__sleepMax = sleepMax
        self.setName("Producer")
        
    def run(self):
        """Announce start-up, sleep, and write to shard cell
        the given number of times, and announce completion."""
        print("%s startting up" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self.__sleepMax))
            self.__cell.setData(count + 1)
        print("%s is done producing" % self.getName())

class Consumer(Thread):
    """Represents a consumer."""
    def __init__(self, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Consumer")
        self._accessCount = accessCount
        self.__cell = cell
        self.__sleepMax = sleepMax
        self.setName("Consumer")
        
    def run(self):
        """Announce start-up, sleep, and read from shard cell
        the given number of times, and announce completion."""
        print("%s startting up" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self.__sleepMax))
            value = self.__cell.getData()
        print("%s is done consuming" % self.getName())

def main():
    """Get the number of accesses from the user,
    create a shared cell, and create and start up
    a producer and a consumer"""
    accessCount = int(input("Enter the number of accesses: "))
    sleepMax = 4
    cell = SharedCell()
    producer = Producer(cell, accessCount, sleepMax)
    consumer = Consumer(cell, accessCount, sleepMax)
    print("Starting the threads")
    producer.start()
    consumer.start()

if __name__ == '__main__':
	main()
