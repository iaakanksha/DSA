stack = []
def push_element():
    if len(stack)==n:
        print('stck overflowed')
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print('Element added')
        print(stack)

def pop_element():
    if not stack:
        print('Stack is empty')
    else:
        e = stack.pop()
        print('Removed element:',e)
        print(stack)

n = int(input('Enter the limit of stack:'))
while True:
    print('Select the option 1. push 2.pop 3. quit')
    choice = int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print('Choose the correct option')
    
    
