class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        top_k = c.most_common()
        top_k.sort(key=lambda x: (-x[1], x[0]))
        return [w for w, _ in top_k[:k]]
