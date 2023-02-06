impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        let n: i32 = (nums.len() as i32) / 2;
        for i in 0..n as usize {
            res.push(nums[i]);
            res.push(nums[(n as usize)+i]);
        }
        return res;
    }
}
