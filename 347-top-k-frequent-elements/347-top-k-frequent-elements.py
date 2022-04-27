class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        lenNums = len(nums)
        freqLists = [[] for _ in range(lenNums + 1)]
        for n in nums:
            freqmap[n] = 1 + freqmap.get(n, 0)
        for nb, count in freqmap.items():
            freqLists[count].append(nb)
        
        res = []
        lenRes = 0
        for i in range(lenNums, 0, -1):
            for n in freqLists[i]:
                res.append(n)
                lenRes += 1
                if lenRes == k:
                    return res