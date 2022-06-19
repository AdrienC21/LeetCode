from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d = defaultdict(list)
        # availaible prefix
        prefixs = [searchWord[:(i+1)] for i in range(len(searchWord))]
        prefixs_set = set(prefixs)
        for w in products:
            for i in range(len(w)):
                prefix = w[:(i+1)]
                if prefix in prefixs_set:
                    d[prefix].append(w)
                    d[prefix].sort()
                    if len(d[prefix]) > 3:
                        d[prefix].pop()
                else:
                    break
        res = []
        for prefix in prefixs:
            res.append(d[prefix])
        return res
