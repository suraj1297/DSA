class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def get(self, value):

        node = self.head
        index = 0
        while node:
            if node.data == value:
                return [node.data, index]
            node = node.next
            index+=1
        
        return None
            

    def add(self, value: int) -> None:
        newNode = Node(value)
        if self.head == None:
            node = newNode
            self.head = node
        else:
            node = self.head
            while node.next:
                node = node.next
            
            node.next = newNode
        self.size +=1
    
    def addAtFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size +=1

    def insertAt(self, index, value):
        if index == 0:
            self.addAtFront(value)
        elif index < self.size:
            newNode = Node(value)
            count = 0
            node = self.head

            while count < index-1:
                node = node.next
                count +=1
            
            newNode.next = node.next
            node.next = newNode
            self.size +=1
            
        else:
            print("Index out of bound")
        
        

    def getList(self) -> None:

        if self.head:
            node = self.head

            while node:
                print(node.data, end=", ")
                node = node.next
            print()
        else:
            print("Linked List is empty")
        
    def delete(self, index= None):
        if index and index >= self.size:
            print('Index out of bound')
        else:
            if index == 0:
                node = self.head
                self.head = node.next
                del node

            elif index and index < self.size-1:
                count = 0
                node = self.head

                while count < index -1:
                    node = node.next
                    count+=1

                node.next = node.next.next
            
            else:

                node = self.head
                prev = None

                while node.next:
                    prev = node
                    node = node.next
                del node
                prev.next = None
            self.size -=1

ll = LinkedList()

ll.getList()
ll.add(5)
ll.add(4)
ll.add(3)
ll.addAtFront(3)
ll.insertAt(3, 10)
ll.insertAt(0, 11)
ll.getList()
ll.delete()
ll.getList()
ll.delete(0)
ll.getList()
ll.delete(1)
ll.getList()
ll.delete(3)
ll.getList()

print(ll.get(10))
print(ll.get(3))
print(ll.get(4))
print(ll.get(11))