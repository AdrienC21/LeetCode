from functools import cmp_to_key
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort by number of taller people in front. In case of equality, sort by height increasing if number of people taller is equal to 0, else sort by height decreasing
        def cmp(x, y):
            if x[1] == y[1]:
                if not(x[1]):
                    return x[0] - y[0]
                return y[0] - x[0]
            return x[1] - y[1]
        key = cmp_to_key(cmp)
        people.sort(key=key)
        # then, add the people iteratively
        res = []
        # first, people with no person higher than them in front
        # sorted by increasing height
        for j, p in enumerate(people):
            if not(p[1]):
                res.append(p)
            else:
                break
        else:  # if no people remaining, return
            return res

        # then the others. We insert them at the beginning, then move to the right until we reached k people taller in front of them
        for i in range(j, len(people)):
            p = people[i]
            h, k = p
            index = 0  # index in res
            count_larger = 0  # people taller than pi in front of pi
            while (count_larger < k) and (index < len(res)):
                if h <= res[index][0]:
                    count_larger += 1
                index += 1
            res.insert(index, p)
        return res
