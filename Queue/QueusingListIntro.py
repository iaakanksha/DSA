 queue = []
>>> queue.append(19)
>>> queue.append(27)
>>> queue.append(76)
>>> queue
[19, 27, 76]
>>> queue.pop(0)
19
>>> queue.pop(0)
27
>>> # pop(0) is used to remove th eelements from front position of the queue otherwise it will act as stack
>>> # to enter elements from front side (enqueue method) we used INSERT method with index number
>>> 
>>> queue = []
>>> queue.insert(0,15)
>>> queue.insert(0,54)
>>> queue.insert(0,52)
>>> queue
[52, 54, 15]
>>> # now to remove elements from tail side
>>> queue.pop()
15
>>> queue.pop()
54
>>> #to check elements at front at rear index we use the index values 0 and -1 respectively
>>> 
>>> q = []
>>> q.append(19)
>>> q.append(76)
>>> q.append(54)
>>> q.append(23)
>>> q[0]
19
>>> q
[19, 76, 54, 23]
>>> q[0]
19
>>> q[-1]
23
>>> # to check whether the queue is empty or not
>>> qu=[]
>>> not qu
True
>>> #it shows true because we have used the negation here as not
>>> 
>>> 