class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dic = {}
        for i, c in enumerate(colors):
            if c in dic:
                dic[c][1] = i
            else:
                dic[c] = [i, i]
        max_dist = 0
        color_list = list(dic.keys())
        for i in range(len(color_list)):
            for j in range(1, len(color_list)):
                c1 = color_list[i]
                c2 = color_list[j]
                for k in range(2):
                    for l in range(2):
                        max_dist = max(max_dist, abs(dic[c1][k] - dic[c2][l]))
        return max_dist