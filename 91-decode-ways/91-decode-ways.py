class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decoded = [None for _ in range(n)]
        for i in range(n):
            if s[-(i+1)] == '0':
                pass
            elif int(s[-(i+1)]) > 2:
                decoded[-(i+1)] = decoded[-i] if i != 0 else 1
            else:
                if i == 0:
                    decoded[-(i+1)] = 1
                elif s[-i] == '0':
                    if i == 1:
                        decoded[-(i+1)] = 1
                    else:
                        decoded[-(i+1)] = decoded[-(i-1)]
                else:
                    decoded[-(i+1)] = 0
                    if i == 1:
                        if not(decoded[-i] is None):
                            decoded[-(i+1)] += decoded[-i]
                        decoded[-(i+1)] += 1 if not((s[-(i+1)] == '2') and (int(s[-i]) > 6)) else 0
                    else:
                        if not(decoded[-i] is None):
                            decoded[-(i+1)] += decoded[-i]
                        if not(decoded[-(i-1)] is None):
                            decoded[-(i+1)] += decoded[-(i-1)] if not((s[-(i+1)] == '2') and (int(s[-i]) > 6)) else 0
        return decoded[0] if not(decoded[0] is None) else 0
