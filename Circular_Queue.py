class Queue:
    def __init__(self,size):
        self.size = size
        self.q = []
        self.front = 0
        self.rear = 0
        for i in range(self.size):
            self.q.append(0)

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if (self.rear+1)%self.size == self.front:
            return True
        else:
            return False

    def Enqueue(self,item):
        if self.is_full() == True:
            print("Queue is Full")
            return
        else:
            self.rear = (self.rear+1)%self.size
            self.q[(self.rear)%self.size] = item

    def Dequeue(self):
        if self.is_empty() == True:
            print("Queue is empty")
            return
        else:
            value = self.q[(self.front+1)%self.size]
            self.front = (self.front+1)%self.size
            return value

    def peek(self):
        if self.is_empty() == True:
            print("Queue is empty")
            return
        else:
            return self.q[self.front]

q = Queue(5)

q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)

print(q.q)
