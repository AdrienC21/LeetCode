from collections import deque
class MyStack:

    def __init__(self):
        self.d1 = deque()

    def push(self, x: int) -> None:
        self.d1.appendleft(x)

    def pop(self) -> int:
        return self.d1.popleft()

    def top(self) -> int:
        return self.d1[0]

    def empty(self) -> bool:
        return not(self.d1)    


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()