class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n+1)]
        for k in range(n // 3):
            answer[3*(k+1) - 1] = "Fizz"
        for k in range(n // 5):
            answer[5*(k+1) - 1] = "Buzz"
        for k in range(n // 15):
            answer[15*(k+1) - 1] = "FizzBuzz"
        return answer
    # Solution try everything
    """
    def fizzBuzz(self, n: int) -> List[str]:
        answer = n * [""]
        for i in range(1, n+1):
            if (i % 3) == 0:
                if (i % 5) == 0:
                    res = "FizzBuzz"
                else:
                    res = "Fizz"
            elif (i % 5) == 0:
                res = "Buzz"
            else:
                res = str(i)
            answer[i-1] = res
        return answer
    """
