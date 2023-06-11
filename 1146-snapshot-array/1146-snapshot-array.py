class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]  # snap 0 initialized with 0
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        snap = self.array[index][-1]  # get last snap
        if snap[0] == self.snaps:  # update val
            snap[1] = val
        else:  # add new val
            self.array[index].append([self.snaps, val])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_left(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]

# Memory Limit Exceeded
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.array = length * [0]
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        res = len(self.snaps)
        self.snaps.append(self.array[:])
        return res

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]
"""


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
