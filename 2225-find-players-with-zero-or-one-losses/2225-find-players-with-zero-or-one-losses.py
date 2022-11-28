class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        has_lost = set()
        has_lost_twice = set()
        for w, l in matches:
            players.add(w)
            players.add(l)
            if l in has_lost:
                has_lost_twice.add(l)
            has_lost.add(l)
        return [sorted(list(players.difference(has_lost))), sorted(list(has_lost.difference(has_lost_twice)))]
