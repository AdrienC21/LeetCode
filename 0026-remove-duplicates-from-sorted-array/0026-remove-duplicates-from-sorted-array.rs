impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i: usize = 1;
        let n: usize = nums.len();
        for j in 1..n {
            if (nums[j] != nums[j-1]) {
                nums[i] = nums[j];
                i += 1;
            }
        }
        return i as i32;
    }
}
