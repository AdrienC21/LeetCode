class StockSpanner:

    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        if not(self.prices):  # span 1
            self.prices.append(price)
            self.spans.append(1)
            return 1
        if price < self.prices[-1]:  # span 1
            self.spans.append(1)
            self.prices.append(price)
            return 1
        span = 1
        i = len(self.prices) - 1
        while (i >= 0) and (self.prices[i] <= price):
            span += self.spans[i]
            i = len(self.prices) - span
        self.spans.append(span)
        self.prices.append(price)
        return span

# it's consecutive days, so this algo below doesn't work
"""
class StockSpanner:

    def __init__(self):
        self.prices = []
    
    def dicho(self, x: int) -> None:
        i = 0
        j = len(self.prices)
        while i < j:
            m = (i + j) // 2
            if self.prices[m] <= x:
                i = m + 1
            else:
                j = m
        span = i + 1
        self.prices.insert(i, x)
        return span

    def next(self, price: int) -> int:
        return self.dicho(price)
"""

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)