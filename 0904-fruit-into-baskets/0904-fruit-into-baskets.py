class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return len(fruits)
        max_fruits = 1
        tree1 = fruits[0]
        tree2 = -1
        basket1 = 1
        basket1_if_new = 1  # count values in a row
        basket2 = 0
        basket2_if_new = 1  # count values in a row
        for i in range(1, n):
            if (fruits[i] != tree1) and (fruits[i] != tree2):
                if fruits[i-1] == tree1:  # replace tree2
                    basket2 = 1
                    basket2_if_new = 1
                    tree2 = fruits[i]
                    basket1 = basket1_if_new
                else:  # replace tree1
                    basket1 = 1
                    basket1_if_new = 1
                    tree1 = fruits[i]
                    basket2 = basket2_if_new
            else:
                if fruits[i] == tree1:
                    basket1 += 1
                    if fruits[i-1] != tree1:
                        basket1_if_new = 1
                    else:
                        basket1_if_new += 1
                else:
                    basket2 += 1
                    if fruits[i-1] != tree2:
                        basket2_if_new = 1
                    else:
                        basket2_if_new += 1
            # update the max
            max_fruits = max(max_fruits, basket1 + basket2)
        return max_fruits
