impl Solution {
    pub fn get_slope(p1: &Vec<i32>, p2: &Vec<i32>) -> f64 {
        if (p1[0] == p2[0]) {
            return f64::MAX;
        }
        return ((p2[1] - p1[1]) as f64) / ((p2[0] - p1[0]) as f64);
    }
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        let slope: f64 = Solution::get_slope(&coordinates[0], &coordinates[1]);
        for i in 2..coordinates.len() as usize {
            if (Solution::get_slope(&coordinates[0], &coordinates[i]) != slope) {
                return false;
            }
        }
        return true;
    }
}