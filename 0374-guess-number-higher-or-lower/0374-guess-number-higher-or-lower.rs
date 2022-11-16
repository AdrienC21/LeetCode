/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut i: i32 = 1;
        let mut j: i32 = n;
        let mut m: i32 = (i / 2) + (j / 2);
        if ((i % 2 == 1) & (j % 2 == 1)) {
            m += 1;
        }
        let mut g: i32 = guess(m);
        while (g != 0) {  // not found
            if (g == (-1)) {
                j = m - 1;
            }
            else {
                i = m + 1;
            }
            m = (i / 2) + (j / 2);
            if ((i % 2 == 1) & (j % 2 == 1)) {
                m += 1;
            }
            g = guess(m);
        }
        return m;
    }
}