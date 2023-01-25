class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        res = 0
        d = deque()  # positions to explore
        d.append(1)
        seen = set()
        n2 = n**2  # to avoid computing it all the time
        
        # fill a 1D versio of the board
        board1D = (n2 + 1) * [0]
        for i in range(n):
            base_pos = n * (n - 1 - i)
            if (n - i) % 2 == 1:  # odd line
                base_pos += 1
                for j in range(n):
                    board1D[base_pos + j] = board[i][j]
            else:
                base_pos += n
                for j in range(n):
                    board1D[base_pos - j] = board[i][j]

        while d:  # explore positions
            res += 1
            for _ in range(len(d)):
                curr = d.popleft()
                for next_pos in range(curr + 1, min(curr + 6, n2) + 1):
                    if board1D[next_pos] > 0:  # ladder or snake
                        destination = board1D[next_pos]  # take it
                    else:
                        destination = next_pos
                    if destination == n2:
                        return res
                    if destination not in seen:
                        d.append(destination)
                        seen.add(destination)

        return -1  # no path to the last cell
