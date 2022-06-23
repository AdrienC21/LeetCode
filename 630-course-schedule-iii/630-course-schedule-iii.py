import heapq
class Solution:
    # I failed ...
    # Trick: sort by lastDay,
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        heapq.heapify(heap)  # we will add negative values, it's a max heap
        total = 0  # total duration of the chosen courses
        courses.sort(key=lambda x: x[1])  # sort by lastDay
        for duration, lastDay in courses:
            if duration + total <= lastDay:  # we can take the course
                total += duration
                heapq.heappush(heap, -duration)
            elif heap and -heap[0] > duration:  # remove the longest course to fit this new one
                total += duration + heapq.heappop(heap)
                heapq.heappush(heap, -duration)
        return len(heap)
