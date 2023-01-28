# Complexity:
# Time: O(k)
# Space: O(k) worst case scenario?
# Where k in the number of numbers seen so far
# So for n numbers O(n^2) space and time?
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        if value in self.seen:  # already seen
            return None
        if not(self.intervals):  # no interval yet
            self.intervals.append([value, value])
            return None
        if value == (self.intervals[0][0] - 1):  # increase first interval
            self.intervals[0][0] = value
            return None
        if value < (self.intervals[0][0] - 1):  # new lowest integer so far
            self.intervals = [[value, value]] + self.intervals
            return None
        if value == (self.intervals[-1][1] + 1):  # increase last interval
            self.intervals[-1][1] = value
            return None
        if value > (self.intervals[-1][1] + 1):  # new largest integer so far
            self.intervals.append([value, value])
            return None
        # All the other intervals
        for index in range(len(self.intervals)):
            inter = self.intervals[index]
            if value == (inter[0] - 1):
                self.intervals[index] = [value, inter[1]]
                return None
            elif value == (inter[1] + 1):
                # do we overlap with the interval above also?
                if (value + 1) == self.intervals[index+1][0]:
                    self.intervals[index] = [inter[0], self.intervals[index+1][1]]
                    self.intervals = self.intervals[:(index+1)] + self.intervals[(index+2):]
                else:
                    self.intervals[index] = [inter[0], value]
                return None
            elif (value > inter[1]) and (value < (self.intervals[index+1][0] - 1)):  # insert value alone here
                self.intervals = self.intervals[:(index+1)] + [[value, value]] + self.intervals[(index+1):]
                return None
            # else, continue and look at the next interval
        return None

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()