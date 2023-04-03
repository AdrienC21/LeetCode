class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        n = len(people)
        i = 0
        j = n - 1
        while i <= j:
            if (people[j] + people[i]) <= limit:
                i += 1
            j -= 1
            res += 1
        return res
