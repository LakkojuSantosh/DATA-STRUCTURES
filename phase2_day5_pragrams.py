"""#logic : first element will be compared with rest
#then second will be compared with rest all..goes
#maintain two parameters and move
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def get_prev_node(self,ref_node):
        current=self.head
        while (current and current.next!=ref_node):
            current=current.next
        return current
    def remove(self,node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head=self.head.next
        else:
            prev_node.next=node.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
def remove_duplicates(llist):
    current1=llist.head
    while current1:
        data=current1.data
        current2=current1.next
        while current2:
            if current2.data==data:
                llist.remove(current2)
            current2=current2.next
        current1=current1.next
a_llist=LinkedList()
data_list=input("Please Enter the elements in the linked list : ").split()
for data in data_list:
    a_llist.append(int(data))
remove_duplicates(a_llist)
print("The list with duplicates removed : ")
a_llist.display()"""


#------------------------------------------------------------------------------------------------
#sll implementation
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):"""



###########################################################################################

'''class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild = None
        self.rightchild = None
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)

node1.leftchild = node2
node1.rightchild = node3
node2.leftchild = node4
node2.rightchild = node5
node3.leftchild = node6
node3.rightchild = node7

print("Root node is : ",node1.data)
print("Left child of the  Root node is : ",node1.leftchild.data)
print("Right child of the Root node is : ",node1.rightchild.data)
print("Left sub root node is : ",node2.data)
print("Left child of the  left sub root node is : ",node2.leftchild.data)
print("Right child of the left sub root node is : ",node2.rightchild.data)
print("Right sub root node is : ",node3.data)
print("Left child of the  right sub root node is : ",node3.leftchild.data)
print("Right child of the right sub root node is : ",node3.rightchild.data)


#                                              50
#                              _________________|____________________
#                             |                                      |
#                            20                                      45
#                     _______|______                            _______|_______
#                    |              |                          |               |
#                   11              15                        30               78
'''
'''
# Inorder Traversal Ex:1

#                                               A
#                              _________________|____________________
#                             |                                      |
#                            B                                       C
#                     _______|______                            _______|_______
#                    |              |                          |               |
#                    D              E                          F               G
# Inorder traversal : D,B,E,A,F,C,G
# Preorder traversal : A,B,D,E,C,F,G
# postorder Traversal : D,E,B,F,G,C,A

#Inorder Traversal Ex:2
#                                              15
#                              _________________|____________________
#                             |                                      |
#                            24                                      54
#                     _______|                                  _______|_______
#                    |                                         |               |
#                   35                                        62               13
# Inorder Traversal : 35,24,15,62,54,13
# Preorder Traversal : 15,24,35,54,62,13
#postorder Traversal : 35,24,62,13,54,15


#Preorder Traversal Ex:1
#                                              45
#                              _________________|____________________
#                             |                                      |
#                            25                                      75
#                     _______|______
#                    |              |
#                   15              35
# Preorder Traversal : 45,25,15,35,75
# Inorder Traversal : 15,25,35,45,75
# postorder Traversal : 


#Post order Traversal Ex:
#                                               1
#                              _________________|____________________
#                             |                                      |
#                            2                                        3
#                     _______|______                            _______|_______
#                    |              |                          |               |
#                    4              5                          6               7
#                               ____|                                     _____|_____
#                              |                                         |           |
#                              8                                         9           10
# Preorder Traversal : 1,2,4,5,8,3,6,7,9,10
# Inorder Traversal : 4,2,8,5,1,6,3,9,7,10
# Postorder Traversal : 
'''


'''######################################TREES######################################'''
'''#Binary tree Traversal Types --> inorder,preorder,postorder
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=" ")
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        #first recur on left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        # then print the data of node
        print(root.val, end=" ")
def printPreorder(root):
    if root:
        #First print the data of node
        print(root.val,end=" ")
        #then recur on left child
        printPreorder(root.left)
        #Finally recur on right child
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE - ORDER : ")
printPreorder(root)
print()
print("\nIN - ORDER : ")
printInorder(root)
print()
print("\nPost - ORDER : ")
printPostorder(root)
print()
'''
'''----################################################'''

'''
# BST - INSERT

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
# a new node with the given key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val < key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)


#                                        (50)
#                                        /   \
#                                       /     \
#                                     (20)     (70)
#                                       \      /  \
#                                        \    /    \
#                                       (40)  (60)  (80)
'''

'''###########################################################'''




