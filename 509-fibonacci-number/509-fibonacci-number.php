class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n) {
        $phi = (1 + sqrt(5)) / 2;
        return round(pow($phi, $n) / sqrt(5));
    }
}