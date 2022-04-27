class Solution:
    """
    l start on the left
    r start on the right
    
    if n odd, l(n) = l(n-1)
    if n%4=2:
        l(n) = 4 * l((n-2)/4)
    else:
        l(n) = 2 * r(n/2). r(n) = 2 l(n/2) -1 so l(n) = 4 * l(n/4) - 2
        where g(n) = same ex with (1, 3, 5, 7 ... n)
    """
    def lastRemaining(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        elif n % 2 == 1:
            return self.lastRemaining(n - 1)
        elif n % 4 == 2:
            return 4 * self.lastRemaining((n - 2) // 4)
        else:
            return 4 * self.lastRemaining(n // 4) - 2