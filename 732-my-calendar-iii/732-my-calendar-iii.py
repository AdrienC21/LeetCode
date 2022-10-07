class MyCalendarThree:

    def __init__(self):
        self.keys = []
        self.events = {}
        self.max_k_booking = 0

    def book(self, start: int, end: int) -> int:
        if start in self.events:
            self.events[start]["start"] += 1
        else:
            keys = self.keys
            bisect.insort_left(keys, start)
            self.keys = keys
            self.events[start] = {"start": 1, "end": 0}
        if end in self.events:
            self.events[end]["end"] += 1
        else:
            keys = self.keys
            bisect.insort_left(keys, end)
            self.keys = keys
            self.events[end] = {"start": 0, "end": 1}
        self.max_k_booking = max(self.max_k_booking, self.calc_k_max())
        return self.max_k_booking
            
    def calc_k_max(self) -> int:
        k_max = 0
        count = 0
        for k in self.keys:
            count -= self.events[k]["end"]
            count += self.events[k]["start"]
            k_max = max(k_max, count)
        return k_max

    # first fail
    """
import random as rd
import sys
class MyCalendarThree:

    def __init__(self):
        self.max_k_booking = 1
        self.events = []
        self.ids = set()

    def book(self, start: int, end: int) -> int:
        event_id = rd.randint(0, sys.maxsize)
        while event_id in self.ids:
            event_id = rd.randint(0, sys.maxsize)
        self.ids.add(event_id)
        L = self.events
        i, L = self.insert(L, start, event_id, "left")
        j, L = self.insert(L, end, event_id, "right")
        self.events = L
        k = 1
        bookings = set()
        bookings.add(event_id)
        for other_id in range(i+1, j):
            if L[other_id][1] not in bookings:
                bookings.add(L[other_id][1])
                k += 1
            
        self.max_k_booking = max(k, self.max_k_booking)
        return self.max_k_booking

    def insert(self, L: list, start: int, event_id: int, side: str):
        if not(L):
            L.append((start, event_id))
            return (0, L)
        n = len(L)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if L[m][0] < start:
                i = m + 1
            else:
                j = m - 1
        k = max(i, j)
        l = min(i, j)
        pos = k  # to insert element
        if side == "left":
            if ((k >= 0) and (k < n) and (L[k][0] < start)):
                pos = k + 1
        else:
            if ((k >= 0) and (k < n) and (L[k][0] <= start)):
                pos = k + 1
        L.insert(pos, (start, event_id))
        return (pos, L)
    """
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)