# Version adapted
# not 100% optimized for the freq map
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = {}
        self.capacity = capacity
        self.min = 0
        self.freq_map = {1: []}

    def get(self, key: int) -> int:
        if not(self.capacity) or (key not in self.cache):
            return -1
        # increase freq of the key
        prev_freq = self.freq[key]
        self.freq_map[prev_freq].remove(key)
        self.freq[key] += 1

        if (prev_freq == self.min) and not(self.freq_map[prev_freq]):
            self.min += 1
        if self.freq[key] not in self.freq_map:
            self.freq_map[self.freq[key]] = []
        self.freq_map[self.freq[key]].append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if not(self.capacity):
            return None
        # if key already exists
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return None

        # remove the LFU
        # add the new one in cache
        # if the cache exceeds the capacity
        if len(self.cache) >= self.capacity:
            prev_key = self.freq_map[self.min][0]
            self.freq_map[self.min].remove(prev_key)
            del self.freq[prev_key]
            del self.cache[prev_key]
        self.cache[key] = value
        self.freq[key] = 1
        self.min = 1
        self.freq_map[self.min].append(key)

# TLE ...
"""
class LFUCache:

    def __init__(self, capacity: int):
        self.current_time = 0  # increase when we put a new key
        self.time = {}
        self.cache = {}
        self.freq = {}
        self.capacity = capacity
        self.current_capacity = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.freq[key] += 1
            self.time[key] = self.current_time
            self.current_time += 1
            return self.cache[key]
        return -1

    def remove_lfu(self) -> None:
        min_freq = sys.maxsize
        times = []
        for key, f in self.freq.items():
            if f < min_freq:
                min_freq = f
                times = [[key, self.time[key]]]
            elif f == min_freq:
                times.append([key, self.time[key]])
        least_recently_used = sys.maxsize
        key_invalidated = None
        for key, t in times:
            if t < least_recently_used:
                least_recently_used = t
                key_invalidated = key
        del self.time[key_invalidated]
        del self.cache[key_invalidated]
        del self.freq[key_invalidated]
    
    def put(self, key: int, value: int) -> None:
        if not(self.capacity):  # nothing to remove
            return None
        if key not in self.cache:
            if self.current_capacity == self.capacity:  # full
                self.remove_lfu()
                self.current_capacity -= 1
            self.current_capacity += 1
            self.freq[key] = 0
        self.cache[key] = value  # update or insert
        self.freq[key] += 1
        self.time[key] = self.current_time
        self.current_time += 1
"""

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)