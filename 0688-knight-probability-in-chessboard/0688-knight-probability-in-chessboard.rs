impl Solution {
    pub fn get_moves(i: i32, j: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut d1_list: Vec<i32> = Vec::new();
        let mut d2_list: Vec<i32> = Vec::new();
        d1_list.push(-1);
        d1_list.push(1);
        d2_list.push(-2);
        d2_list.push(2);
        for d1 in &d1_list {
            for d2 in &d2_list {
                let mut to_add: Vec<i32> = Vec::new();
                to_add.push(i+d1);
                to_add.push(j+d2);
                res.push(to_add);
                let mut to_add: Vec<i32> = Vec::new();
                to_add.push(i+d2);
                to_add.push(j+d1);
                res.push(to_add);
            }
        }
        return res;
    }
    pub fn rec_search(i: i32, j: i32, l: i32, n: i32, k: i32, dp: &mut Vec<Vec<Vec<f64>>>) -> f64 {
        if ((i < 0) || (i >= n) || (j < 0) || (j >= n)) {
            return 0.
        }
        if (l >= k) {
            return 1.;
        }
        if (dp[i as usize][j as usize][l as usize] != -1.0) {
            return dp[i as usize][j as usize][l as usize];
        }
        let mut res: f64 = 0.;
        let mut a: i32;
        let mut b: i32;
        let moves: Vec<Vec<i32>> = Solution::get_moves(i, j);
        for move_id in 0..8 as usize {
            a = moves[move_id][0];
            b = moves[move_id][1];
            res += (1. / 8.) * Solution::rec_search(a, b, l+1, n, k, dp);
        }
        dp[i as usize][j as usize][l as usize] = res;
        return res;
    }
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        let mut dp: Vec<Vec<Vec<f64>>> = Vec::new();
        for i in 0..n {
            let mut add_row: Vec<Vec<f64>> = Vec::new();
            for j in 0..n {
                let mut add_col: Vec<f64> = Vec::new();
                for l in 0..k {
                    add_col.push(-1.0);
                }
                add_row.push(add_col);
            }
            dp.push(add_row);
        }

        return Solution::rec_search(row, column, 0, n, k, &mut dp);
    }
}
