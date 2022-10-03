class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        streak_color = colors[0]  # current color
        max_time = neededTime[0]  # max time of the current color
        sum_time = neededTime[0]  # sum of time of the current color
        streak = 1  # number of balloons from the current color
        for id_c in range(1, len(colors)):
            c = colors[id_c]
            if c != streak_color:  # if color changes
                streak_color = c  # new color
                if streak != 1:  # if streak was k ballons>=2, remove k-1 ballons with min cost (so sum - max)
                    streak = 1
                    total_time += sum_time - max_time
                max_time = neededTime[id_c]
                sum_time = neededTime[id_c]
            else:  # update the streak
                streak += 1
                max_time = max(max_time, neededTime[id_c])
                sum_time += neededTime[id_c]
        # check the last streak
        if streak != 1:
            streak = 1
            total_time += sum_time - max_time
        return total_time
