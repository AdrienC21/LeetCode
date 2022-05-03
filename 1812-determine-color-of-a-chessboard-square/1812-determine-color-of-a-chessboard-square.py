class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ((ord(coordinates[0]) - ord("a")) % 2) == 0:  # white if number (row) is even
            res_mod = 0
        else:  # white if number (row) is odd
            res_mod = 1
        return (int(coordinates[1]) % 2) == res_mod