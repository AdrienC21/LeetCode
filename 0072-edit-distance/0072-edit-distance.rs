use std::cmp;

impl Solution {
    // Use Dynamic programming
    // O(n1*n2), n1 = len(word1), n2 = len(word2)
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let n1: i32 = word1.len() as i32;
        let n2: i32 = word2.len() as i32;
        let w1_vec: Vec<char> = word1.chars().collect();
        let w2_vec: Vec<char> = word2.chars().collect();
        let mut dp: Vec<Vec<i32>> = Vec::new();
        for i in 0..(n1+1) {
            let mut new_vec: Vec<i32> = Vec::new();
            for j in 0..(n2+1) {
                new_vec.push(i32::MAX);
            }
            dp.push(new_vec);
        }
        for j in 0..(n2+1) as usize {
            dp[n1 as usize][j] = n2 - (j as i32);
        }
        for i in 0..(n1+1) as usize {
            dp[i][n2 as usize] = n1 - (i as i32);
        }
        
        for i in (0..(n1)).rev() {
            for j in (0..(n2)).rev() {
                if (w1_vec[i as usize] == w2_vec[j as usize]) {
                    dp[i as usize][j as usize] = dp[(i as usize)+1][(j as usize)+1]
                }
                else {
                    dp[i as usize][j as usize] = 1 + cmp::min(dp[(i as usize)+1][(j as usize)+1], cmp::min(dp[(i as usize)+1][j as usize], dp[(i as usize)][(j as usize)+1]));
                }
            }
        }
        return dp[0][0];
    }
}
