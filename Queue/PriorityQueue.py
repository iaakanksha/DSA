#method 1
q = []
q.append(10)
q.append(30)
q.append(56)
q.append(63)
q.sort()
q.pop()#here highest value has high priority
q.pop(0)#here lowest value has low priority


#method 2
import queue
q1 = queue.PriorityQueue()
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)

q1.get()
q1.get()
q1.get()
