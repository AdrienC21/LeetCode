class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {"{}".format(chr(x)): [-1, -1] for x in range(97, 97+26)}
        n = len(s)
        for i, v in enumerate(s):
            if d[v][0] == -1:
                d[v][0] = i
                d[v][1] = i
            else:
                d[v][1] = i

        current_id = 0
        res = []
        while current_id < n:
            c = s[current_id]
            last_id = d[c][1]
            if last_id == (n - 1):
                res.append(last_id - current_id + 1)
                break
            new_last_id = -1
            new_last_id_update = True
            while new_last_id_update:
                new_last_id_update = False
                for i in range(current_id, max(last_id, new_last_id)+1):
                    letter = s[i]
                    if (d[letter][1] != -1) and (d[letter][1] > new_last_id):
                        new_last_id = d[letter][1]
                        new_last_id_update = True
            last_id = new_last_id
            res.append(last_id - current_id + 1)
            current_id = last_id + 1

        return res