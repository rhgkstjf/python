class LinkedList:
    class Node:
        def __init__(self,item,link):
            self.item = item
            self.link = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self,item):
        if self.is_empty():
            self.head = self.Node(item,None)
        else:
            self.head = self.Node(item,self.head)
        self.size += 1

    def insert_after(self,item,n):
        n.link = self.Node(item,n.link)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            print("list is empty")
        else:
            self.head = self.head.link
            self.size -= 1

    def delete_after(self,n):
        if self.is_empty():
            print("list is empty")
        else:
            t = n.link
            n.link = t.link
            self.size -= 1
    def search(self,target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.link
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.link != None:
                print(p.item,' -> ',end = ' ')
            else:
                print(p.item)
            p = p.link
            

s = LinkedList()
s.insert_front("hello")
s.insert_after("my name is hanseol",s.head)
s.insert_front("hi")
print(s.search("hi"))
s.print_list()

    
