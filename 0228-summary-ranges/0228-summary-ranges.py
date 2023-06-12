class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not(nums):
            return []
        ranges = []
        current_range = nums[0]
        current_nb = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] == (current_nb + 1):
                current_nb += 1
            else:
                if current_range == current_nb:
                    ranges.append(f"{current_nb}")
                else:
                    ranges.append(f"{current_range}->{current_nb}")
                current_range = nums[i]
                current_nb = nums[i]
        if current_range == current_nb:
            ranges.append(f"{current_nb}")
        else:
            ranges.append(f"{current_range}->{current_nb}")
        
        return ranges
