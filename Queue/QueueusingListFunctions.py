queue = []
def enqueue():
    element = input('Enter the element to add:')
    
    queue.append(element)
    print('Yayyy Element'+ element +'is added in the queue!!')

def dequeue():
    if not queue:
        print('Queue is empty :(')
    else:
        e = queue.pop(0)#removing element from front position
        print('Element' + e + 'is removed!!')

def display():
    print(queue)

while True:
    print('Select operation 1.Add 2.Remove 3.Show 4.Quit')
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print('Kindly enter valid choice!!')
