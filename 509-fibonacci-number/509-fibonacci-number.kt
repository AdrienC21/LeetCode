import kotlin.math.*
class Solution {
    fun fib(n: Int): Int {
        val sqrt5: Double = sqrt(5.toDouble());
        val phi: Double = (1 + sqrt5) / 2;
        val res: Double = round(phi.pow(n.toDouble()) / sqrt5);
        return res.toInt();
    }
}