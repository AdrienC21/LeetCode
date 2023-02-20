impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let n: i32 = nums.len() as i32;
        let mut i: i32 = 0;
        let mut j: i32 = n - 1;
        let mut m: i32;
        while (i < j) {
            m = i + (j - i) / 2;
            if (nums[m as usize] == target) {
                return m;
            }
            else if (nums[m as usize] < target) {
                i = m + 1;
            }
            else {
                j = m - 1;
            }
        }
        if (j < 0) {
            return 0;
        }
        if (nums[i as usize] < target) {
            return i + 1;
        }
        return i;
    }
}