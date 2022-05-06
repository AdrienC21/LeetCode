class Solution:
    # Trick: in practice, recursion or stacks when we want to remove things!
    def removeDuplicates(self, s: str, k: int) -> str:
        L = list(s)  # will be modified in place
        stack = [0]  # indices of the new letters
        n = len(s)
        i = 1  # indice of the letter in the word without duplicates
        j = 1  # indice of the letter in the original word (s)
        while j < n:
            L[i] = L[j]  # if we removed letters, need to update in real time the values in L
            if (i == 0) or (L[i-1] != L[i]):  # new character
                stack.append(i)
            elif (i - stack[-1] + 1) == k:  # k-duplicated characters
                i = stack.pop() - 1  # -1 because of the +1 after
            i += 1
            j += 1  # go to next character
        return "".join(L[:i])  # return the modified string (length of i)
    # iterative solution, time limit exceeded on long strings
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        no_duplicated_found = False
        L = list(s)
        while not(no_duplicated_found):  # while we found a duplicate, let's continue
            n = len(L)
            i = 0
            k_duplicated = False  # if we don't enter the while loop below, work shorter than k so exit the program
            while (i < (n-k+1)):
                c = L[i]  # current character
                j = i + 1
                k_duplicated = True
                while k_duplicated and (j <= (i + k - 1)):
                    if L[j] == c:
                        j += 1
                    else:
                        k_duplicated = False
                if k_duplicated:
                    break
                i = j
            if k_duplicated:  # drop the duplicate from L
                L = L[:i] + L[j:]
            else:  # no duplicate found
                no_duplicated_found = True
        return "".join(L)
    """