class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for v in nums:
            if v in s:  # a pair is formed
                s = s.difference(set([v]))
            else:  # create new pair with one element atm
                s.add(v)
        if not(s):
            return True
        return False