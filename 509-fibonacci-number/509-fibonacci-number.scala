object Solution {
    def fib(n: Int): Int = {
        val phi = (1 + math.sqrt(5)) / 2;
        val res = math.round(math.pow(phi, n) / math.sqrt(5));
        return res.toInt;
    }
}