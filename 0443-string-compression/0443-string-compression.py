class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        i = 1  # pointer in chars
        j = 0  # pointer in modified chars
        current_group = chars[0]
        len_group = 1
        while i < n:
            if chars[i] == current_group:
                len_group += 1
            else:
                if len_group >= 2:
                    chars[j] = current_group
                    len_group_str = str(len_group)
                    for k in range(j+1, j+1+len(len_group_str)):
                        chars[k] = len_group_str[k-j-1]
                    j += 1 + len(len_group_str)
                else:
                    chars[j] = current_group
                    j += 1
                current_group = chars[i]
                len_group = 1
            i += 1
        if len_group >= 2:
            chars[j] = current_group
            len_group_str = str(len_group)
            for k in range(j+1, j+1+len(len_group_str)):
                chars[k] = len_group_str[k-j-1]
            j += 1 + len(len_group_str)
        else:
            chars[j] = current_group
            j += 1
        # delete the extra elements in chars
        for _ in range(j, n):
            chars.pop()
        return j
