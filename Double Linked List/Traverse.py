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
                n = n.ref          

    #for backward traversal
    def print_LL_reverse(self):
        if self.head is None:
            print('Linked list is empty :( ')
        else:
            n = self.head
            while n.nref is not None:
                print(n.data,"->",end="")
                n= n.pref
               
dl1 = DoubleLL()
dl1.print_LL() 
dl1.print_LL_reverse()          