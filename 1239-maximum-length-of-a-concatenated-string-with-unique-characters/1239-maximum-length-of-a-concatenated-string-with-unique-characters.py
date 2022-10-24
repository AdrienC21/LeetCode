class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def recSearch(arr: List[str], s: Set[chr]):
            if not(arr):
                return len(s)
            if len(s) == 26:
                return 26
            first_word_set = arr[0]
            if not(first_word_set.intersection(s)):  # intersection empty
                union = first_word_set.union(s)
                return max(recSearch(arr[1:], union), recSearch(arr[1:], s))
            # else, just skip the word
            return recSearch(arr[1:], s)
        arr_set = [set(x) for x in arr if len(x) == len(set(x))]
        return recSearch(arr_set, set())
