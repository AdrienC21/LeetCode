class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for n in arr2:
            dic[n] = 0
        dic["other"] = []
        for n in arr1:
            if n in dic:
                dic[n] += 1
            else:
                dic["other"].append(n)
        res = []
        for n in arr2:
            res.extend(dic[n] * [n])
        res.extend(sorted(dic["other"]))
        return res
