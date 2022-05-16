class Solution {
public:
    int arrangeCoins(int n) {
        double delta = n;
        delta = delta * 8;
        delta = delta + 1;
        return int((-1 + sqrt(delta)) / 2);
    }
};