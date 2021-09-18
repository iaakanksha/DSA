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
                print(n.data,"->",end = '' )
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node  

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
   
    def add_betweenafter(self,data,x):
        n = self.head
        while n is not None: #this while loop is used to traverse through and find the x node after which we have to add the new node
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('node is not present in LL')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_end(500)
LL1.add_betweenafter(200,100)
LL1.add_begin(20)
LL1.print_LL()

