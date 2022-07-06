func fib(n int) int {
    var phi = (1 + math.Sqrt(5)) / 2;
    var n_float = float64(n);
    var res = math.Round(math.Pow(phi, n_float) / math.Sqrt(5));
    return int(res);
}