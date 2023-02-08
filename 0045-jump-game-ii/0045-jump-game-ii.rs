use std::cmp;


impl Solution {
    pub fn recSearch(i: usize , nums: &Vec<i32>, n: &i32, dp: &mut Vec<i32>) -> i32 {
        if (dp[i] == -1) {  // never calculated
            let maxJump: i32 = nums[i];
            let mut res: i32 = *n + 1;
            for j in (1..(cmp::min(maxJump+1, *n-(i as i32)))).rev() {
                res = cmp::min(res, 1 + Solution::recSearch(i+(j as usize), nums, n, dp));
            }
            dp[i] = res;
        }
        return dp[i];
    }
    pub fn jump(nums: Vec<i32>) -> i32 {
        let n: i32 = nums.len() as i32;
        let mut dp: Vec<i32> = Vec::new();
        for i in 0..n {
            dp.push(-1);
        }
        dp[(n-1) as usize] = 0;

        return Solution::recSearch(0 as usize, &nums, &n, &mut dp);
    }
}
