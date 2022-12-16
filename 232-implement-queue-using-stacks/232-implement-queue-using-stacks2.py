class MyQueue:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        self.l2.append(x)

    def pop(self) -> int:
        if not(self.l1):
            self.process_stacks()
        return self.l1.pop()

    def peek(self) -> int:
        if not(self.l1):
            self.process_stacks()
        return self.l1[-1]

    def empty(self) -> bool:
        return not(self.l1) and not(self.l2)
    
    def process_stacks(self) -> None:
        while self.l2:
            self.l1.append(self.l2.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
