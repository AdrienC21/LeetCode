impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let m: i32 = grid.len() as i32;
        let n: i32 = grid[0].len() as i32;
        let mut r: i32 = n;
        let mut res: i32 = 0;
        for i in (0..m).rev() {
            for j in 0..r {
                if (grid[i as usize][(n-1-j) as usize] < 0) {
                    res += 1;
                }
                else {
                    r = j;
                    break;
                }
            }
            if (r == 0) {
                break;
            }
        }
        return res;
    }
}
