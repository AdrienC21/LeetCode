use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let n: i32 = nums.len() as i32;
        let threshold: i32 = n / 2;
        let mut counter: HashMap<i32, i32> = HashMap::new();
        for i in 0..n {
            let mut num: i32 = nums[i as usize];
            counter.insert(num, 1 + if counter.contains_key(&num) { counter[&num] } else { 0 });
            if (counter[&num] > threshold) {
                return num;
            }
        }
        return 0;
    }
}
