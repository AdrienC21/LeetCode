use std::cmp;

impl Solution {
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        let mut res: i32 = nums[0];
        let mut running_mean: f64 = nums[0] as f64;
        let mut running_count: f64 = 1 as f64;
        for i in 1..(nums.len()) {
            running_count = running_count + (1 as f64);
            running_mean = running_mean + ((nums[i as usize] as f64) - running_mean) / running_count;
            res = cmp::max(res, (running_mean.ceil()) as i32);
        }
        return res;
    }
}
