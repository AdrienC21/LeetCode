class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        nb_letters_zigzag = (2 * numRows - 2)
        nb_complete_zigzags = (len(s) // nb_letters_zigzag)
        numCols = (numRows - 1) * nb_complete_zigzags
        if len(s) % nb_letters_zigzag > numRows:
            numCols += (1 + ((len(s) % nb_letters_zigzag) - numRows))  # incomplete last zigzag, add more columns
        else:
            numCols += 1
        m = [["" for _ in range(numCols)] for _ in range(numRows)]
        
        p = 0  # pointer on the string
        
        # Draw the zigzag
        for zigzag in range(nb_complete_zigzags):  # draw the complete zigzag
            j = (numRows - 1) * zigzag
            for i in range(numRows):
                m[i][j] = s[p]
                p += 1
            for k in range(1, numRows - 1):
                m[i-k][j+k] = s[p]
                p += 1
        
        # Draw the last incomplete zigzag
        if len(s) % nb_letters_zigzag > numRows:
            j = (numRows - 1) * nb_complete_zigzags
            for i in range(numRows):
                m[i][j] = s[p]
                p += 1
            remaining_letters = len(s) - nb_complete_zigzags * nb_letters_zigzag - numRows
            for k in range(remaining_letters):
                m[i-(k+1)][j+k+1] = s[p]
                p += 1
        else:
            remaining_letters = len(s) - nb_complete_zigzags * nb_letters_zigzag
            j = (numRows - 1) * nb_complete_zigzags
            for i in range(remaining_letters):
                m[i][j] = s[p]
                p += 1
            
        # Collect the final word
        final_word = []
        for i in range(numRows):
            for j in range(numCols):
                if not(m[i][j] == False):  # it's a letter
                    final_word.append(m[i][j])
        return "".join(final_word)
