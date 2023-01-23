class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trusted = defaultdict(set)
        who_trust = defaultdict(set)
        for a, b in trust:
            trusted[b].add(a)  # b trusted by a
            who_trust[a].add(b)  # a trust b
        judge = None
        for b in trusted:
            if len(trusted[b]) == (n-1):  # trusted by all the others
                if judge is not None:  # if someone validate already this property
                    return -1
                judge = b  # else it's a judge
        if judge is None:  # no judge
            return -1
        if not(who_trust[judge]):  # judge doesn't trust someone so property 1 OK
            return judge
        return -1  # else no judge
