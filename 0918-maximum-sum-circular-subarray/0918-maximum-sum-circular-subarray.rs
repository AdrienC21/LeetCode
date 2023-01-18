use std::cmp;

impl Solution {
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        let mut tot_sum: i32 = nums.iter().sum();
        let mut current_min: i32 = 0;  // min running sum
        let mut current_max: i32 = 0;
        let mut tot_min: i32 = i32::MAX;  // min of all running sum
        let mut tot_max: i32 = i32::MIN;

        for n in &nums {
            current_min = cmp::min(current_min + *n, *n);
            current_max = cmp::max(current_max + *n, *n);
            tot_min = cmp::min(tot_min, current_min);
            tot_max = cmp::max(tot_max, current_max);
        }
        
        if (tot_max <= 0) {
            return tot_max;
        }
        return cmp::max(tot_max, tot_sum - tot_min);
    }
}