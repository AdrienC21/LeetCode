impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut to_reach: usize = nums.len() - 1;  // init at last index
        for i in (0..(nums.len()-1)).rev() {
            if ((i + (nums[i] as usize)) >= to_reach) {
                to_reach = i;
            }
        }
        return (to_reach == 0);
    }
}
