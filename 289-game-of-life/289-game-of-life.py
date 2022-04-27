class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        0 become 0 => 0
        0 become 1 => 2
        1 become 0 => 3
        1 become 1 => 1
        """
        
        m = len(board)
        n = len(board[0])
        if (m == 1) and (n == 1):
            board[0][0] = 0
        elif m == 1:
            if board[0][0] == 1:
                board[0][0] = 3
            else:
                board[0][0] = 0
            if board[0][n-1] == 1:
                board[0][n-1] = 3
            else:
                board[0][n-1] = 0
            for j in range(1, n-1):
                if board[0][j] != 0:
                    nb_live_neighbors = 0
                    if board[0][j-1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[0][j+1] in [1, 3]:
                        nb_live_neighbors += 1
                    if nb_live_neighbors < 2:
                        board[0][j] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[0][j] = 1
                    else:
                        board[0][j] = 3
            for j in range(n):
                if board[0][j] == 2:
                    board[0][j] = 1
                elif board[0][j] == 3:
                    board[0][j] = 0
        elif n == 1:
            if board[0][0] == 1:
                board[0][0] = 3
            else:
                board[0][0] = 0
            if board[m-1][0] == 1:
                board[m-1][0] = 3
            else:
                board[m-1][0] = 0
            for i in range(1, m-1):
                if board[i][0] != 0:
                    nb_live_neighbors = 0
                    if board[i-1][0] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i+1][0] in [1, 3]:
                        nb_live_neighbors += 1
                    if nb_live_neighbors < 2:
                        board[i][0] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[i][0] = 1
                    else:
                        board[i][0] = 3
            for i in range(m):
                if board[i][0] == 2:
                    board[i][0] = 1
                elif board[i][0] == 3:
                    board[i][0] = 0
        else:
            # corner upper left
            if board[0][0] == 0:
                if (board[1][0] in [1, 3]) and (board[1][1] in [1, 3]) and (board[0][1] in [1, 3]):
                    board[0][0] = 2
            else:
                nb_live_neighbors = 0
                if board[0][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][0] in [1, 3]:
                    nb_live_neighbors += 1
                if nb_live_neighbors < 2:
                    board[0][0] = 3
                elif nb_live_neighbors in [2, 3]:
                    board[0][0] = 1
                else:
                    board[0][0] = 3

            # corner upper right
            if board[0][n-1] == 0:
                if (board[1][n-1] in [1, 3]) and (board[1][n-2] in [1, 3]) and (board[0][n-2] in [1, 3]):
                    board[0][n-1] = 2
            else:
                nb_live_neighbors = 0
                if board[1][n-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[0][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if nb_live_neighbors < 2:
                    board[0][n-1] = 3
                elif nb_live_neighbors in [2, 3]:
                    board[0][n-1] = 1
                else:
                    board[0][n-1] = 3
            
            # corner down left
            if board[m-1][0] == 0:
                if (board[m-2][0] in [1, 3]) and (board[m-2][1] in [1, 3]) and (board[m-1][1] in [1, 3]):
                    board[m-1][0] = 2
            else:
                nb_live_neighbors = 0
                if board[m-2][0] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-1][1] in [1, 3]:
                    nb_live_neighbors += 1
                if nb_live_neighbors < 2:
                    board[m-1][0] = 3
                elif nb_live_neighbors in [2, 3]:
                    board[m-1][0] = 1
                else:
                    board[m-1][0] = 3
            
            # corner down right
            if board[m-1][n-1] == 0:
                if (board[m-1][n-2] in [1, 3]) and (board[m-2][n-2] in [1, 3]) and (board[m-2][n-1] in [1, 3]):
                    board[m-1][n-1] = 2
            else:
                nb_live_neighbors = 0
                if board[m-1][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][n-1] in [1, 3]:
                    nb_live_neighbors += 1
                if nb_live_neighbors < 2:
                    board[m-1][n-1] = 3
                elif nb_live_neighbors in [2, 3]:
                    board[m-1][n-1] = 1
                else:
                    board[m-1][n-1] = 3
            
            # line left
            for i in range(1, m-1):
                nb_live_neighbors = 0
                if board[i-1][0] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i-1][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i+1][1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i+1][0] in [1, 3]:
                    nb_live_neighbors += 1
                
                if board[i][0] == 0:
                    if nb_live_neighbors == 3:
                        board[i][0] = 2
                else:
                    if nb_live_neighbors < 2:
                        board[i][0] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[i][0] = 1
                    else:
                        board[i][0] = 3
            
            # line right
            for i in range(1, m-1):
                nb_live_neighbors = 0
                if board[i-1][n-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i-1][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i+1][n-2] in [1, 3]:
                    nb_live_neighbors += 1
                if board[i+1][n-1] in [1, 3]:
                    nb_live_neighbors += 1
                
                if board[i][n-1] == 0:
                    if nb_live_neighbors == 3:
                        board[i][n-1] = 2
                else:
                    if nb_live_neighbors < 2:
                        board[i][n-1] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[i][n-1] = 1
                    else:
                        board[i][n-1] = 3
            
            # line up
            for j in range(1, n-1):
                nb_live_neighbors = 0
                if board[0][j-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][j-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][j] in [1, 3]:
                    nb_live_neighbors += 1
                if board[1][j+1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[0][j+1] in [1, 3]:
                    nb_live_neighbors += 1
                
                if board[0][j] == 0:
                    if nb_live_neighbors == 3:
                        board[0][j] = 2
                else:
                    if nb_live_neighbors < 2:
                        board[0][j] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[0][j] = 1
                    else:
                        board[0][j] = 3
            # line down
            for j in range(1, n-1):
                nb_live_neighbors = 0
                if board[m-1][j-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][j-1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][j] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-2][j+1] in [1, 3]:
                    nb_live_neighbors += 1
                if board[m-1][j+1] in [1, 3]:
                    nb_live_neighbors += 1
                
                if board[m-1][j] == 0:
                    if nb_live_neighbors == 3:
                        board[m-1][j] = 2
                else:
                    if nb_live_neighbors < 2:
                        board[m-1][j] = 3
                    elif nb_live_neighbors in [2, 3]:
                        board[m-1][j] = 1
                    else:
                        board[m-1][j] = 3
            
            # middle
            for i in range(1, m-1):
                for j in range(1, n-1):
                    nb_live_neighbors = 0
                    if board[i-1][j-1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i-1][j] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i-1][j+1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i][j+1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i+1][j+1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i+1][j] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i+1][j-1] in [1, 3]:
                        nb_live_neighbors += 1
                    if board[i][j-1] in [1, 3]:
                        nb_live_neighbors += 1
                    
                    if board[i][j] == 0:
                        if nb_live_neighbors == 3:
                            board[i][j] = 2
                    else:
                        if nb_live_neighbors < 2:
                            board[i][j] = 3
                        elif nb_live_neighbors in [2, 3]:
                            board[i][j] = 1
                        else:
                            board[i][j] = 3
            
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 2:
                        board[i][j] = 1
                    elif board[i][j] == 3:
                        board[i][j] = 0