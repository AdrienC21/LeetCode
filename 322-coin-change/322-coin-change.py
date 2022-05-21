import sys
class Solution:
    # better solution ... O(amount*|coins|), dynamic programming, store the solution of 1 coin, then 2 coins, then etc until solution
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic programming initialization
        dp = [sys.maxsize for _ in range(amount+1)]
        dp[0] = 0
        l = len(coins)

        # fill the dp array!
        for i in range(1, amount+1):
            # test: include all the coins, one by one
            for j in range(l):
                if coins[j] <= i:  # coin less that amount i
                    rest = dp[i-coins[j]]
                    # update dp if taking this coin gives smaller value 
                    if (rest != sys.maxsize) and ((rest + 1) < dp[i]):
                        dp[i] = rest + 1
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]

    # Recursive solution, but time exceeded
    """
    # find directly the coins lower than amount (else the initial array can be to big)
    def findMax(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if coins[m] == amount:
                return m
            elif coins[m] < amount:
                i = m + 1
            else:
                j = m - 1
        return max(i, j)

    # Recursive function
    def findAmount(self, coins: List[int], amount: int) -> int:
        if not(amount):
            return 0
        if not(coins):
            return -1
        if len(coins) == 1:
            if coins[0] == amount:
                return 1
            a = amount / coins[0]
            if a == int(a):  # select multiple time coins[0] to obtain amount
                return int(a)
            return -1
        if coins[-1] == amount:
            return 1
        change1 = self.findAmount(coins[:-1], amount)
        new_amount = amount - coins[-1]
        j = len(coins) - 1
        while (j >= 0) and (coins[j] > new_amount):
            j -= 1
        if j < 0:
            change2 = -1
        else:
            change2 = self.findAmount(coins[:(j+1)], new_amount)
        if (change1 == -1) and (change2 == -1):
            return -1
        elif change1 == -1:
            return 1 + change2  # because we used one coin
        elif change2 == -1:
            return change1
        else:
            return min(change1, 1 + change2)

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        m = self.findMax(coins, amount)
        return self.findAmount(coins[:(m+1)], amount)
    """
