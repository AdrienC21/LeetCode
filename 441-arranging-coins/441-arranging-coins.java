class Solution {
    public int arrangeCoins(int n) {
        double delta = n;
        delta = 1 + 8 * delta;
        double res = ((-1 + Math.sqrt(delta)) / 2);
        int final_res = (int)res;
        return final_res;
    }
}