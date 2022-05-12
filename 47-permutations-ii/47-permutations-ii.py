class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            sub_res = self.permuteUnique(nums[1:])
            s = set()
            len_permu = len(sub_res[0])
            for permu in sub_res:
                for index in range(len_permu+1):
                    new_permu = permu[:]
                    new_permu.insert(index, nums[0])
                    s.add(tuple(new_permu))
            return list(map(lambda x: list(x), list(s)))