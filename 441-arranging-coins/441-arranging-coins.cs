public class Solution {
    public int ArrangeCoins(int n) {
        double delta = n;
        delta = delta * 8 + 1;
        double res = (-1 + Math.Sqrt(delta)) / 2;
        int final_res;
        final_res = Convert.ToInt32(Math.Floor(res));
        return final_res;
    }
}