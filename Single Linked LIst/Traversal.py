class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None #ref is NONE because we are just creating a single node

class LinkedList:
    def __init__(self):
        self.head = None #head is None because we are creating the head of the list
    
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty :( ')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.print_LL()

