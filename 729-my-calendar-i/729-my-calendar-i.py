class MyCalendar:

    def __init__(self):
        self.booked = []

    def dicho(self, n: int):
        i = 0
        j = len(self.booked)
        while i < j:
            m = (i + j) // 2
            if self.booked[m] < n:
                i = m + 1
            elif self.booked[m] > n:
                j = m - 1
            else:
                return m + 1
        res = max(i, j)
        if (res < len(self.booked)) and (self.booked[res] <= n):
            return res + 1
        return res

    def book(self, start: int, end: int) -> bool:
        n = self.dicho(start)
        if n % 2 == 1:  # start of the event is between two already booked event
            return False
        else:
            if n == len(self.booked):
                self.booked.insert(len(self.booked), start)
                self.booked.insert(len(self.booked), end)
                return True
            elif end > self.booked[n]:  # events overlap
                return False
            else:
                self.booked.insert(n, end)
                self.booked.insert(n, start)
                return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)