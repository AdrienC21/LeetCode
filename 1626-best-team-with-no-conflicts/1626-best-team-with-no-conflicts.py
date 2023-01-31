class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        dp = n * [0]  # dp[i] max score of team that includes play i
        L = sorted(zip(ages, scores))  # sort by age first

        for i, (_, score) in enumerate(L):
            dp[i] = score
            for j in range(i):
                if score >= L[j][1]:  # if a younger player has a higher score, try to include him
                    dp[i] = max(dp[i], dp[j] + score)

        return max(dp)
