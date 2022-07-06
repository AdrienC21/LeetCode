class Solution {
    func fib(_ n: Int) -> Int {
        let phi = Double((1 + sqrt(5)) / 2);
        let n = Double(n);
        let res = Double(round(pow(phi, n) / sqrt(5)));
        return Int(res);
    }
}