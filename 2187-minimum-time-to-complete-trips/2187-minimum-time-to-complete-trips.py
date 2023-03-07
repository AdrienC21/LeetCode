class Solution:
    # Trick, binary search ...
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 1  # min number of time
        j = min(time) * totalTrips  # max number of time

        while i < j:
            m = i + (j - i) // 2
            trips = 0  # count trips for that time
            for t in time:
                trips += m // t
            if trips >= totalTrips:
                j = m  # "at least", so j = m, not m - 1
            else:
                i = m + 1
        return i

    # Tried an implementation using a deque
    """
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        max_time = max(time)
        d = deque(max_time * [[]])
        for t in time:
            d[t-1].append(t)
        trips = 0
        min_time = 0
        while trips < totalTrips:
            min_time += 1
            trips += sum(d[0])
            d.append([])
            for t in d[0]:
                d[t].append(t)
            d.popleft()
        return min_time
    """

    # TLE
    """
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        for i, t in enumerate(time):
            time[i] = [t, 0]  # time necessary / current time travelled by bus i
        trips = 0  # trips made
        min_time = 0  # time necessary
        while trips < totalTrips:
            min_time += 1  # increase time
            for i, (t, c) in enumerate(time):
                if (c + 1) == t:  # bus i completed a trip
                    time[i][1] = 0
                    trips += 1
                else:
                    time[i][1] += 1
        return min_time
    """
