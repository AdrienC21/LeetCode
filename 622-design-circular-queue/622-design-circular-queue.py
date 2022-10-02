class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.front = 0
        self.rear = 0
        self.len = k

    def enQueue(self, value: int) -> bool:  # add to the rear
        if self.isFull():
            return False
        if not(self.queue[self.rear] is None):
            self.rear = (self.rear - 1) % self.len
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:  # remove from the front
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        if self.front != self.rear:
            self.front = (self.front - 1) % self.len
        return True

    def Front(self) -> int:
        if not(self.queue[self.front] is None):
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if not(self.queue[self.rear] is None):
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return (self.front == self.rear) and (self.queue[self.front] is None)

    def isFull(self) -> bool:
        return (((self.front == (self.len - 1)) and (self.rear == 0)) or (self.front == (self.rear - 1))) and not(self.queue[self.front] is None) and not(self.queue[self.rear] is None)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()