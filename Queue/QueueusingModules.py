
#module 1
#module name=collections & class name = deque 

import collections
q = collections.deque()
#deque is used to add elements at both side of the queue here
q.appendleft(10)
q.appendleft(29)
q.appendleft(39)
#appendleft is used to add elements at front end of the queue here
q.popleft()
q.pop()


#module 2
#module name=queue & class name = Queue

import queue
q = queue.Queue()
q.put(19)
q.put(26)
q.put(45)
q.put(25)

q.get()
q.get()
 
