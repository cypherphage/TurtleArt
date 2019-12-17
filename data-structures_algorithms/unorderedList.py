from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.end = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.head == None:
            self.end = temp
        self.head = temp
        

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        prev = current
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                temp = current.getNext()
                prev.setNext(temp)
                current.setNext(None)                
            prev = current
            current = current.getNext()

    def index(self,item):
        current = self.head
        count = -1
        while current != None:
            count = count + 1
            if current.getData() == item:
                break
            current = current.getNext()
        return count


    def __str__(self):
        current = self.head
        linkedList = ""
        while current != None:
            linkedList = linkedList + "-->" + str(current.getData()) 
            current = current.getNext()
        return linkedList

    def pop(self,pos):
        x = self.size()
        count = -1
        if pos > x - 1 or pos < 0:
            return "Index out of range"
        else:
            current = self.head
            while count != pos:
                count = count + 1
                out = current.getData()
                current = current.getNext()
            return out
    
    def end_item(self):
        return self.end.getData()

    def append(self,item):
        temp = Node(item)
        temp1 = self.end
        temp1.setNext(temp)
        self.end = temp

    def insert(self,item,pos):
        current = self.head
        count = 0
        if pos > self.size() or pos < 0:
            return "index out of range"
        else:
            if pos == 0:
                temp = Node(item)
                temp1 = self.head
                self.head = temp
                temp.setNext(temp1)
            else:
                while count < pos - 1:
                    count = count + 1
                    current = current.getNext()
                temp = Node(item)
                temp1 = current.getNext()
                current.setNext(temp)
                temp.setNext(temp1)

            


                
            





