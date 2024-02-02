class stak :
    def __init__(self): #سيلف بتشاور ع الاوبجكت
        self.items=[]
    def push (self,item): # السيلف هنا عشان اعرف الاوبجكت
        self.items.append(item)  
    def pop (self,item):
        self.items.pop(item)     
    def size (self):
        return len(self.items)
    def peek  (self):    # اخر عنصر
        return self.items[-1]
    def impty (self):
        return self.items==[]
    #lilo
    

srr=stak()
srr.push(2)
srr.push(6)
srr.push(55)
print(srr.items)
srr.pop(-1)
print(srr.items)
print(srr.size())
print(srr.peek())
print(srr.impty())
