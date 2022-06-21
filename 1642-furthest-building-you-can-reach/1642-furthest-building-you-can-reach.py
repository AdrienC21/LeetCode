class Solution:
    # use all the ladders (heap to store differences), then use the bricks!
    # no more bricks, return the current index pos
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders:
                    heappush(heap, diff)
                    ladders -= 1
                elif heap and diff > heap[0]:
                    heappush(heap, diff)
                    bricks -= heappop(heap)
                else:
                    bricks -= diff
                if bricks < 0:
                    return i
        return (n - 1)
    # first try, but it fails on example 2 :/
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ups = [0]  # list of floors to climb
        arrivals = []  # at which index you arrive if you climb up[i]
        for i, h in enumerate(heights):
            if i > 0:
                if h > heights[i-1]:
                    arrivals.append(i-1)
                    ups.append(h - heights[i-1])
        arrivals.append(len(heights)-1)
        # then, use all the bricks, and iteratively replace the biggest ups with ladders + use the saved bricks
        index_up = 0
        bricks_used = 0
        while (index_up < len(ups)) and (bricks_used + ups[index_up] <= bricks):
            bricks_used += ups[index_up]
            index_up += 1
        remaining_bricks = bricks - bricks_used
        ups_list = sorted(ups[:index_up])
        while ladders and (index_up < len(ups)):
            ladders -= 1
            biggest_up = ups_list.pop()
            remaining_bricks += biggest_up
            while (index_up < len(ups)) and (remaining_bricks >= ups[index_up]):
                remaining_bricks -= ups[index_up]
                ups_list.append(ups[index_up])
                index_up += 1
            ups_list.sort()  # sort again the ups
        index_up -= 1
        return arrivals[index_up]
    """
