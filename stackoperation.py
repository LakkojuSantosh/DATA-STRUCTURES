#stack implementation
#Stack is LIFO  -  Last In First Out
stack=[]
def push():
    element=int(input("Enter the element : "))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("Removed element : ",e)
        print(stack)
while True:
    print("Select Operation 1.push  2.pop  3.Quit")
    choice=int(input("Enter : "))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the valid operation🤪🤪🤪🤪")