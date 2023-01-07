class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        # else: a solution exists
        n = len(gas)
        gas_tank = 0
        res = 0
        for i in range(n):
            gas_tank += (-cost[i] + gas[i])
            if gas_tank < 0:  # res can't be the initial start
                gas_tank = 0  # empty gas tank
                res = i + 1  # test if an issue occur starting from i + 1
        return res

    # TLE O(n^2) ...
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        L = [-cost[i]+gas[i+1] for i in range(n-1)] + [-cost[n-1]+gas[0]]
        if sum(L) < 0:
            return -1
        for i in range(n):
            if gas[i] >= cost[i]:  # ok candidate
                res = gas[i] + L[i]
                j = (i + 1) % n
                while (res >= 0) and (j != i) and (res >= cost[j]):
                    res += L[j]
                    j += 1
                    j %= n
                if j == i:
                    return i
        return -1
    """
