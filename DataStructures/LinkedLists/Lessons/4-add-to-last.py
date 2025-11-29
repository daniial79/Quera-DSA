class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode
        

class LinkedList:
    def __init__(self, node=None):
        self.head = node 
        self.tail = node 
        self.size = 0 if self.head is None else 1
        
    def traverse(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next
            
    def search(self, aim):
        itr = self.head
        while itr is not None:
            if itr.data == aim:
                print("Found it!")
                break
            itr = itr.next
            
def addFirst(self, value):
    newNode = Node(value)

    if self.head is None:
        self.head = newNode
        self.tail = newNode
    else:
        newNode.next = self.head
        self.head = newNode

    self.size += 1 
    
def addLast(self, value):
    newNode = Node(value)
    
    if self.tail is None:
        self.head = newNode
        self.tail = newNode
    else:
        self.tail.next = newNode
        self.tail = newNode
        
    self.size += 1

