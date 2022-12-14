use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n: i32 = nums.len() as i32;
        if (n == 1) {
            return nums[0];
        }
        if (n == 2) {
            return cmp::max(nums[0], nums[1]);
        }
        let mut m1: i32 = cmp::max(nums[(n-2) as usize], nums[(n-1) as usize]);
        let mut m2: i32 = nums[(n-1) as usize];
        let mut temp: i32 = 0;
        for i in (0..(n-2)).rev() {
            temp = cmp::max(nums[i as usize] + m2, m1);
            m2 = m1;
            m1 = temp;
        }
        return m1;
    }
}
