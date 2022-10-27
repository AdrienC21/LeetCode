use std::collections::HashMap;
impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        let mut dic: HashMap<i32, i32> = HashMap::new();
        dic.insert(0, -1);  // pairs cum sum mod k and index
        let mut cum_sum: i32 = 0;
        for i in 0..(nums.len()) {
            let n: i32 = nums[i];
            cum_sum += n;
            let r: i32 = cum_sum % k;
            if (!(dic.contains_key(&r))) {
                dic.insert(r, i as i32);
            }
            else if ((i as i32) - dic[&r] >= 2) {
                return true;
            }
        }
        return false;
    }
}
