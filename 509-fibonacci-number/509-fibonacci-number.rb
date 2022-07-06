# @param {Integer} n
# @return {Integer}
def fib(n)
    phi = (1 + Math.sqrt(5)) / 2;
    return ((phi ** n) / Math.sqrt(5)).round();
end