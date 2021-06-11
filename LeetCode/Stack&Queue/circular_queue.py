class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = k-1
        self.num_items = 0
        self.MAX_LEN = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.MAX_LEN
            self.queue[self.rear] = value
            self.num_items += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.MAX_LEN
            self.num_items -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.num_items == 0

    def isFull(self) -> bool:
        return self.num_items == self.MAX_LEN

