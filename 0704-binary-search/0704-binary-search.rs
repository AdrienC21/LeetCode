impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = (nums.len() - 1) as i32;
        let mut m: i32 = left + (right - left) / 2;
        let mut val: i32;
        while (left < right) {
            val = nums[m as usize];
            if (val == target) {
                return m;
            }
            else if (val < target) {
                left = m + 1;
            }
            else {
                right = m - 1;
            }
            m = left + (right - left) / 2;
        }
        if (left == right) {
            if (nums[left as usize] == target) {
                return left;
            }
        }
        return -1;
    }
}