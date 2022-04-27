class Solution:
    def recTest(self, pushed: List[int], popped: List[int], L: List[int]) -> bool:
        if not(pushed):  # we can only pop
            if not(popped):  # nothing to pop so true
                return True
            else:  # try to pop everything
                for i, _ in enumerate(L):
                    if popped[i] != L[-(i+1)]:
                        return False
                return True
        else:  # we can push
            if not(L):  # nothing to pop from L, we can only push
                return self.recTest(pushed[1:], popped, [pushed[0]])
            else:
                if L[-1] == popped[0]:  # we can pop SO POP BECAUSE ALL THE ELEMENTS ARE UNIQUE!
                    return self.recTest(pushed, popped[1:], L[:-1])
                else:  # pop not possible atm, so push
                    return self.recTest(pushed[1:], popped, L + [pushed[0]])
                
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return self.recTest(pushed, popped, [])