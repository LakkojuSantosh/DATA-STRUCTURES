'''# BST delete -------------------
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
#found in that tree
def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif(key > root.key):
        root.right=deleteNode(root.right,key)
    #if the key is same as root's key , then this is
    #to be deleted
    else:
        #Node with only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        #copy the inorder successor's
        #content to this node
        root.key = temp.key
        #delete the inorder successor
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root, 50)
root=insert(root, 30)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root, 70)
root=insert(root, 60)
root=insert(root, 80)
print("Inorder Traversal of the given Tree : ")
inorder(root)
print("\nDelete 20")
root=deleteNode(root,20)
print("Inorder Traversal of the Modified Tree : ")
inorder(root)
print("\nDelete 30")
root=deleteNode(root,30)
print("Inorder Traversal of the Modified Tree : ")
inorder(root)
print("\nDelete 50")
root=deleteNode(root,50)
print("Inorder Traversal of the Modified Tree : ")
inorder(root)'''


######################################
'''
#import dictionary from graph
from collections import defaultdict
#ADD EDGE TO GRAPH : FUNCTION
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
#FUNCTION DESCRIPTION
def generate_edges(graph):
    edges=[]
    #for each node in graph
    for node in graph:
        for neighbour in graph[node]:
            #if edge exists then append
            edges.append((node,neighbour))
    return edges
#DECLARING - graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
#Printing Graph
print(generate_edges(graph))
'''


########################################################
'''
#Adjacency Matrix
class Graph(object):
    #Initialize the matrix
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size=size
    #add edges
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Same vertex %d and %d" %(v1,v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    #Remove edges
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("No edge between %d and %d" %(v1,v2))
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    def __len__(self):
        return self.size
    #print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val))
            print()
def main():
    g=Graph(5)
    g.add_edge(0,1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_matrix()
if __name__=="__main__":
    main()
'''

###############################################################

'''#----------> Breadth First Search---------------
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
#BFS - we use Queue
visited = []            #List for visited nodes
queue = []              #Initialize a queue
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:                                  #creating loop to visit
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'5')      #Function call
'''


#############################################################
## ----------> Depth First Search------------------
#Using dictionary to act as an adjacency list
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
#BFS - we use Queue
visited = set()           #set to keep track of visited node
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'5')      #Function call
























