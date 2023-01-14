class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        group_id = -1
        d = {}  # match a letter to a group id
        group = defaultdict(set)  # match a group id to all the letters of the group
        for c1, c2 in zip(s1, s2):
            if (c1 not in d) and (c2 not in d):  # new group with the two letters
                group_id += 1
                d[c1] = group_id
                d[c2] = group_id
                group[group_id].add(c1)
                group[group_id].add(c2)
            elif c1 not in d:  # add c1 in group of c2
                current_group = d[c2]
                d[c1] = current_group
                group[current_group].add(c1)
            elif c2 not in d:  # add c2 in group of c1
                current_group = d[c1]
                d[c2] = current_group
                group[current_group].add(c2)
            elif d[c1] == d[c2]:  # letters already in the same group
                continue
            else:  # merge the two groups
                merged_group = d[c1]
                old_group = d[c2]
                group[merged_group] = group[merged_group].union(group[old_group])
                for c in group[old_group]:
                    d[c] = merged_group
                group[old_group] = set()
        # create dict that associat to a group the minimum letter within the group
        letter_attribution = {}
        for g in group:
            if group[g]:
                letter_attribution[g] = min(group[g])
        
        res = ""
        for c in baseStr:
            if c in d:  # if letter in the group, attribute the minimum
                group_of_c = d[c]
                res += letter_attribution[group_of_c]
            else:  # else the letter
                res += c
        return res
