class stak :
    def __init__(self): #سيلف بتشاور ع الاوبجكت
        self.items=[]
    def enqueue (self,item): # السيلف هنا عشان اعرف الاوبجكت
        self.items.append(item)  
    def dequeue (self):
        self.items.pop(0)     
    def size (self):
        return len(self.items)
    def peek  (self):    # اخر عنصر
        return self.items[-1]
    def impty (self):
        return self.items==[]
    #fifo
    

srr=stak()
srr.push(2)
srr.push(6)
srr.push(55)
print(srr.items)
srr.pop()
print(srr.items)
print(srr.size())
print(srr.peek())
print(srr.impty())
        