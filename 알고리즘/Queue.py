class Queue:
    def __init__(self,size):
        self.size = size
        self.q = []
        self.front = 0
        self.rear = 0
        for i in range(self.size):
            self.q.append(0)
    
    def is_full(self):
        if self.rear == self.size:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def Enqueue(self,item):
        if self.is_full() == True:
            print("Queue is full")
            return
        else:
            self.q[self.rear] = item
            self.rear += 1
    
    def Dequeue(self):
        if self.is_empty() == True:
            print("Queue is empty")
            return
        else:
            value = self.q[self.front]
            self.q[self.front] = 0
            self.front += 1
            return value
