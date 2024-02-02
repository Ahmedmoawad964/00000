
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData
        
    def setNext(self, newnext):
        self.next = newnext




node = Node(30)
print(node.getData())
print (node.getNext())


# In[ ]:


class singleList:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
       
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    
    def printList(self):
        current=self.head
        print("list Data")
        while current!=None:
            print(current.getData(),end=" ")
            current=current.getNext()
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and found == False:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()  
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while found == False: #while Not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())      
    
    def isEmpty(self):
        return self.head == None      
    
    def clear(self):
        self.head=None 


# In[ ]:


mylist = singleList()

mylist.add(20)
mylist.add(30)
mylist.add("Kholood Salah")


print("LL size is= ", mylist.size())


print("Is 20 in mylist : ", mylist.search(20))
print("Is 30 in mylist : ", mylist.search(30))
print("Is Kholood Salah in mylist : ", mylist.search("Kholood Salah"))

mylist.remove(30)
mylist.remove(20)
mylist.remove("Kholood Salah")

print("Is 20 in mylist : ", mylist.search(20))
print("Is 30 in mylist : ", mylist.search(30))

mylist.isEmpty()


# In[ ]:


mylist.clear()


# In[ ]:


mylist.printList()

