impl Solution {
    pub fn rec_search(i: usize, j: usize, dp: &mut Vec<Vec<Vec<i32>>>, nums: &Vec<i32>) -> Vec<i32> {
        if (dp[i][j][0] != -1) {
            let mut res: Vec<i32> = Vec::new();
            res.push(dp[i][j][0]);
            res.push(dp[i][j][1]);
            return res;
        }
        // we take i
        let other_player1: Vec<i32> = Solution::rec_search(i+1, j, dp, nums);
        let mut subres1: Vec<i32>;
        if (other_player1[1] == ((i+1) as i32)) {
            subres1 = Solution::rec_search(i+2, j, dp, nums);
        }
        else {  // j
            subres1 = Solution::rec_search(i+1, j-1, dp, nums);
        }
        let subsum1: i32 = subres1[0] + nums[i];

        // we take j
        let other_player2: Vec<i32> = Solution::rec_search(i, j-1, dp, nums);
        let mut subres2: Vec<i32>;
        if (other_player2[1] == (i as i32)) {
            subres2 = Solution::rec_search(i+1, j-1, dp, nums);
        }
        else {  // j-1
            subres2 = Solution::rec_search(i, j-2, dp, nums);
        }
        let subsum2: i32 = subres2[0] + nums[j];

        if (subsum1 >= subsum2) {  // best move is to take i
            let mut to_add: Vec<i32> = Vec::new();
            to_add.push(subsum1);
            to_add.push((i as i32));
            dp[i][j] = to_add;
        }
        else {  // best move is to take j
            let mut to_add: Vec<i32> = Vec::new();
            to_add.push(subsum2);
            to_add.push((j as i32));
            dp[i][j] = to_add;
        }
        let mut res: Vec<i32> = Vec::new();
        res.push(dp[i][j][0]);
        res.push(dp[i][j][1]);
        return res;
    }
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n: i32 = nums.len() as i32;
        let mut dp: Vec<Vec<Vec<i32>>> = Vec::new();  // [score, index to take]
        for i in 0..n {
            let mut to_add: Vec<Vec<i32>> = Vec::new();
            for j in 0..n {
                let mut to_add2: Vec<i32> = Vec::new();
                to_add2.push(-1);
                to_add2.push(-1);
                to_add.push(to_add2);
            }
            dp.push(to_add);
        }

        for i in 0..n as usize {
            dp[i][i][0] = nums[i];
            dp[i][i][1] = (i as i32);
            if (i < ((n as usize) - 1)) {
                if (nums[i] >= nums[i+1]) {
                    dp[i][i+1][0] = nums[i];
                    dp[i][i+1][1] = (i as i32);
                }
                else {
                    dp[i][i+1][0] = nums[i+1];
                    dp[i][i+1][1] = ((i+1) as i32);
                }
            }
        }
        let player_1: Vec<i32> = Solution::rec_search(0, (n as usize)-1, &mut dp, &nums);
        let score_player_1: i32 = player_1[0];
        let total_score: i32 = nums.iter().sum();
        let score_player_2: i32 = total_score - score_player_1;
        return (score_player_1 >= score_player_2);
    }
}
