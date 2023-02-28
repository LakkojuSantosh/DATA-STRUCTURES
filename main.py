'''
#STACK IS LIFO
stack=[]
def push():
    element = int(input("Enter the element :"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element:",e)
        print(stack)
while True:
    print("Select operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice ==2:
        pop_element()
    elif choice ==3:
        break
    else:print("Enter only 1,2 and 3")  '''
#-------------------------------------------------------------------------
'''#Stack
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return  True
        else:
            return False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t = self.head
        if self.isempty():
            print("Stack underflow")
        else:
            while(t != None):
                print(t.data,end=" ")
                t = t.next
                if (t != None):
                    print("-->",end = "")
            print()
            return
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    print("peek value is",s.peek())#peek returns the value of tap element
    s.pop()
    s.pop()
    s.display()
    print("peek value is", s.peek())    '''
#-------------------------------------------------------------------------

'''s = input()
st = []
balanced = True
for char in s:
    if (char=="{" or char =="[" or char =="("):
        st.append(char)

    elif (char == "}"):
        if (len(st) and st.pop() != "{"):
            balanced = False
            break
    elif (char == "]"):
        if (len(st) and st.pop() != "["):
            balanced = False
            break
    elif (char == ")"):
        if (len(st) and st.pop() != "("):
            balanced = False
            break
    else:
        balanced = False
        break
if (balanced == False or len(st)):
    print("Not balanced")
else:
    print("Balanced")   '''
#-------------------------------------------------------------------------
'''#Queue
queue = []
def enqueue():
    element = input("Enter the element")
    queue.append(element)
    print(element,"is aded to the queue")
def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e = queue.pop(0)
        print("Removed element",e)
def display():
    print(queue)
while True:
    print("Select operation 1.add 2.remove 3.show 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice ==4:
        break
    else:
        print("Enter correct value")    '''
#-------------------------------------------------------------------------
#Stack using queue module
'''from queue import LifoQueue
s = LifoQueue(maxsize=3)
print(s.qsize())
s.put("a")
s.put("b")
s.put("c")
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())    '''
#-------------------------------------------------------------------------
'''#Queue using queue module
import queue
L = queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(L.get())
print(L.get())  '''
#Queue using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return  None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
a_queue = Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    #by using split , do will become a list ,split works with string
    do = input("What would you like to do?").split()

    operation = do[0].strip().lower()
    if operation == "enqueue":
        a_queue.enqueue(int(do[1]))
    elif operation == "dequeue":
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print("Queue is empty")
        else:
            print("Dequeued element :",int(dequeued))
    elif operation=="quit":
        break



