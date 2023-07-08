class Solution:
    # not from me
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        max_count = 0
        counter = Counter()  # two keys, 'T' and 'F'

        i = 0
        for j, ans in enumerate(answerKey):
            counter[ans] += 1
            max_count = max(max_count, counter[ans])
            while (max_count + k) < (j - i + 1):
                counter[answerKey[i]] -= 1
                i += 1
            res = max(res, j - i + 1)

        return res
