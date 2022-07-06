public class Solution {
    public int Fib(int n) {
        // use explicit formula
        double phi = (1 + Math.Sqrt(5)) / 2;
        double res = Math.Round(Math.Pow(phi, n) / Math.Sqrt(5));
        return (int) res;
    }
}