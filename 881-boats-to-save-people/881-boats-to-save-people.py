class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        c = Counter(people)
        boats = c[limit]
        isEven = (limit % 2 == 0)
        lowerLim = limit // 2
        remainings = 0
        for i in range(limit-1, lowerLim, -1):
            if c[i] >= c[limit-i]:
                boats += c[i]
                remainings = max(0, remainings - (c[i] - c[limit-i]))
            else:
                boats += c[i]
                remainings += (c[limit-i] - c[i])

        if isEven:
            boats += (c[lowerLim] // 2)
            remainings += (c[lowerLim] % 2)

        if remainings != 0:
            boats += ((remainings + 1) // 2)

        return boats