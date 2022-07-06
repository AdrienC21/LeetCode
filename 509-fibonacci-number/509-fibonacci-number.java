class Solution {
    public int fib(int n) {
        // use explicit formula
        double phi = (1 + Math.sqrt(5)) / 2;
        double res = Math.round(Math.pow(phi, n) / Math.sqrt(5));
        return (int) res;
    }
}