class Solution {
    func arrangeCoins(_ n: Int) -> Int {
        let delta = 1 + 8 * n;
        let sdelta = Double(delta).squareRoot();
        return Int(floor((-1 + sdelta) / 2));
    }
}