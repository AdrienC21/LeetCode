impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let mut i: usize = 0;
        let mut j = nums.len() - 1;
        let mut m: usize;
        while (i < j) {
            m = i + (j - i) / 2;
            if ((m % 2) == 1) {  // even index only
                m -= 1;
            }
            if (nums[m] == nums[m+1]) {
                i = m + 2;
            }
            else {
                j = m;
            }
        }
        return nums[i];
    }
}
