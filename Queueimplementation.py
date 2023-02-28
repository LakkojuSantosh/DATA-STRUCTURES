#Queue
Queue=[]
def enqueue():
    element=int(input("Enter your element : "))
    Queue.append(element)
def dequeue():
    if not Queue:
        print("the queue is empty")
    else:
        e=Queue.pop(0)
        print("Removed element is ",e)
def display():
    print(Queue)
while True:
    print("Select operation 1.add  2.remove  3.show  4.quit")
    choice=int(input("Enter : "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter a valid input")