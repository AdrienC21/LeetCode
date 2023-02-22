class Solution:
    def run_simulation(self, weights: List[int], days: int, max_capacity: int) -> bool:
        day = 1
        running_sum = 0
        i = 0
        n = len(weights)
        while (day <= days) and (i < n):
            if (running_sum + weights[i]) > max_capacity:  # new day
                day += 1
                running_sum = 0
            else:  # update running_sum, process next package later
                running_sum += weights[i]
                i += 1
        return (day <= days)  # if True, we shipped everyting on time
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        i = max(weights)  # minimum capacity to put all the packages
        j = sum(weights)  # maximum capacity (load everything in 1 day)
        while i < (j - 1):
            m = i + (j - i) // 2
            if self.run_simulation(weights, days, m):
                j = m
            else:
                i = m
        while not(self.run_simulation(weights, days, i)):
            i += 1
        return i
