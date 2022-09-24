class Solution:
    def numberOfWays(self, corridor: str) -> int:
        prods = []
        count_seat = 0
        total_count_seat = 0
        i = 0
        n = len(corridor)
        current_dividor = 1
        mod = 10**9 + 7
        while i < n:
            if corridor[i] == "S":
                total_count_seat += 1
                count_seat += 1
                if count_seat == 2:
                    count_seat = 0
                    i += 1
                    current_dividor = 1
                    while (i < n) and (corridor[i] == "P"):
                        current_dividor += 1
                        i += 1
                    prods.append(current_dividor)
                else:
                    i += 1
            else:
                i += 1
        
        if not(prods):
            return 0
        if total_count_seat % 2 == 1:
            return 0
        if len(prods) == 1:
            return 1
        prods.pop()  # remove last one, because no two seats on the right

        res = 1
        while prods:
            res *= prods.pop()
            res = res % mod
        return res
