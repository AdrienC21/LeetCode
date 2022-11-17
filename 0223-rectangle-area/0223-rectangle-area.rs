use std::cmp;
impl Solution {
    pub fn area(x1: i32, x2: i32, y1: i32, y2: i32) -> i32 {
        return (y2 - y1) * (x2 - x1);
    }
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {        
        let tot: i32 = Solution::area(ax1, ax2, ay1, ay2) + Solution::area(bx1, bx2, by1, by2);
        if ((ax2 <= bx1) || (ay1 >= by2) || (ax1 >= bx2) || (ay2 <= by1)) {  // no overlap
            return tot;
        }
        let x: i32 = cmp::min(ax2, bx2) - cmp::max(ax1, bx1);
        let y: i32 = cmp::min(ay2, by2) - cmp::max(ay1, by1);
        return tot - x * y;  // remove intersection
    }
}
