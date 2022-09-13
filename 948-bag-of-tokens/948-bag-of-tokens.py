class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        score = 0
        max_score = 0
        while tokens:
            if tokens[0] <= power:
                power -= tokens.popleft()
                score += 1
                max_score = max(max_score, score)
            elif score >= 1:
                power += tokens.pop()
                score -= 1
            else:
                break
        return max_score
