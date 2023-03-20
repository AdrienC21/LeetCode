class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = len(flowerbed)
        if flowers == 1:
            if (n == 0) or ((n == 1) and (flowerbed[0] == 0)):
                return True
            return False
        for i in range(flowers):
            if n < 1:
                break
            if flowerbed[i] == 0:
                if ((i == 0) and (flowerbed[1] == 0)) or ((i == (flowers - 1)) and (flowers >= 2) and (flowerbed[flowers-2] == 0)) or ((flowerbed[i-1] == 0) and (flowerbed[i+1] == 0)):
                    flowerbed[i] = 1
                    n -= 1
        return (n < 1)
