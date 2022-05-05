class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # let's use two pointers
        pleft = 0
        pright = len(numbers) - 1
        nbleft = numbers[pleft]
        nbright = numbers[pright]
        while pleft < pright:
            s = nbleft + nbright
            if s < target:
                pleft += 1
                nbleft = numbers[pleft]
            elif s > target:
                pright -= 1
                nbright = numbers[pright]
            else:
                return [pleft+1, pright+1]
        return [-1, -1]