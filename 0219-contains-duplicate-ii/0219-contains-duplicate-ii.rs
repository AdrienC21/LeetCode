use std::collections::HashMap;
impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut dic: HashMap<i32, i32> = HashMap::new();
        let size: i32 = (nums.len() as i32);
        for i in 0..size as usize {
            let n: i32 = nums[i];
            if (dic.contains_key(&n)) {
                let j: i32 = dic[&n] as i32;
                if (((i as i32) - j) <= k) {
                    return true;
                }
            }
            dic.insert(n, i as i32);
        }
        return false;
    }
}
