class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None #nref = ref of next node
        self.pref = None #pref = ref of previous node

class DoubleLL:
    def __init__(self):
        self.head = None

    # for forward traversal   
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty :( ')
        else:
            n = self.head
            while n is not None:
                print(n.data,"->",end = '' )
                n = n.nref          

    #for backward traversal
    def print_LL_reverse(self):
        if self.head is None:
            print('Linked list is empty :( ')
        else:
            n = self.head
            while n.nref is not None:
                print(n.data,"->",end="")
                n= n.pref

    # inserting node when list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is empty!")

    # inserting elements at begining
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # inserting at end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n  

    # inserting after a particular node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not available in LL")
        elif n.nref is None:
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.nref.pref = new_node
            new_node.nref = n.nref
            new_node.pref = n 

    # inserting before a particular node
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given node is not available!!")
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node

    # Deletion at beginning
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deletion!!")
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Deletion at end
    def delete_end(self):
        if self.head is None:
            print("DLL is empty!!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty agter deletion!!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # Delete by particular value
    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty!!")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in the list")
            return
        if self.head.data ==x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
              break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is not present in the list")

dl1 = DoubleLL()
dl1.insert_empty(10)
dl1.add_after(20,10)
dl1.add_before(50,20)
dl1.add_end(30)
dl1.delete_by_value(10)
dl1.delete_begin()
dl1.delete_end()

dl1.print_LL() 