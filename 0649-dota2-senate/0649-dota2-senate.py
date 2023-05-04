class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque(list(senate))
        n = len(d)
        nb_d = sum(c == "D" for c in d)
        nb_r = n - nb_d
        
        to_eliminate = 0
        prev = " "
        while nb_d and nb_r:
            if d[0] == prev:
                to_eliminate += 1
                d.append(d.popleft())
            elif to_eliminate:
                d.popleft()
                to_eliminate -= 1
                if prev == "D":
                    nb_r -= 1
                else:
                    nb_d -= 1
            else:
                to_eliminate = 1
                prev = d[0]
                d.append(d.popleft())
        if nb_d:
            return "Dire"
        return "Radiant"
