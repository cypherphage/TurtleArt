from unorderedList import UnorderedList
from node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return UnorderedList.isEmpty(self)
    
    def size(self):
        return UnorderedList.size(self)

    def remove(self,item):
        return UnorderedList.remove(self,item)

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        prev = None
        while current != None:
            if current.getData() > item:
                prev = current
                break
            current = current.getNext()
            



    