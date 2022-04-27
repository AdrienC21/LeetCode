class FreqStack:

    def __init__(self):
        self.freq = {}
        self.eltFreq = {}
        self.topFreq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        freq = self.freq[val] + 1
        self.freq[val] = freq
        
        if freq > self.topFreq:
            self.topFreq = freq
        if freq not in self.eltFreq:
            self.eltFreq[freq] = []
        self.eltFreq[freq].append(val)

    def pop(self) -> int:
        val = self.eltFreq[self.topFreq].pop()
        self.freq[val] -= 1
        if not(self.eltFreq[self.topFreq]):
            self.topFreq -= 1
        
        return val
        

            
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()