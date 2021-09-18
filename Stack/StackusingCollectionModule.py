Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import collections
>>> stack= collections.deque()
>>> stack
deque([])
>>> stack.append(12)
>>> stack.append(12)
>>> stack.append(12)
>>> stack.append(12)
>>> stack.append(11)
>>> stack
deque([12, 12, 12, 12, 11])
>>> stack.pop()
11
>>> stack.pop()
12
>>> 