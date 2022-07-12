class Solution:
    # recursive backtracking approach, not mine
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        n = len(matchsticks)
        if s % 4 != 0:
            return False
        side = s // 4
        matchsticks.sort(reverse=True)  # descending order
        if matchsticks[0] > side:  # at least a match is larger than the side
            return False
        def recSearch(i: int, space_remaining: int, sides_completed: int) -> bool:
            if sides_completed == 3:  # all sides completed
                return True
            while i < n:
                num = matchsticks[i]
                if num > space_remaining:  # skip this match
                    i += 1
                    continue
                matchsticks[i] = side + 1  # we will not use this matchstick
                if num == space_remaining:  # we completed a side
                    res = recSearch(1, side, sides_completed+1)  # start at index 1 because first match is always placed on first side
                else:
                    res = recSearch(i+1, space_remaining-num, sides_completed)
                if res:
                    return True
                matchsticks[i] = num  # put back the original value at index i
                while i < n and matchsticks[i] == num:  # process next value that is different !!
                    i += 1
            return False
        return recSearch(0, side, 0)
    # wrong ...
    """
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        side = s // 4
        square = 4 * [side]
        for match in matchsticks:  # place the match on the sides of the square
            for i, side in enumerate(square):
                if side > match:
                    square[i] -= match
                    break
                elif side == match:
                    square[i] = square[-1]
                    square.pop()
                    break
            else:  # match is to big to be on any side of the square
                return False
        return True
    """
