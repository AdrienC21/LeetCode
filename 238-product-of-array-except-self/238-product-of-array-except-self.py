class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZeros = 0
        prodNoZero = 1
        id_zero = -1
        for i, n in enumerate(nums):
            if n == 0:
                countZeros += 1
                id_zero = i
                if countZeros == 2:
                    return len(nums) * [0]
            else:
                prodNoZero *= n
        if countZeros:  # 1 zero
            return (id_zero * [0]) + [prodNoZero] + ((len(nums) - id_zero - 1) * [0])
        else:
            answer = []
            for n in nums:
                answer.append(prodNoZero // n)
            return answer
