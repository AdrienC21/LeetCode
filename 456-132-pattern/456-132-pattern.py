class Solution:
    # stack solution
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curr_min = nums[0]  # current minimum
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:  # find a j, such that n=nums[k] < nums[j]
                stack.pop()
            if stack and n > stack[-1][1]:  # check if nums[k]=n > nums[i]
                return True
        
            stack.append((n, curr_min))
            curr_min = min(curr_min, n)
        return False
