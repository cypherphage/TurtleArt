class Node:
    def __init__(self,init_data):
        self.next = None
        self.data = init_data

    def setData(self,new_data):
        self.data = new_data
        
    def setNext(self,new_next):
        self.next = new_next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
        