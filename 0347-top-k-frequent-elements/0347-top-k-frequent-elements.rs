use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counter: HashMap<i32, i32> = HashMap::new();
        for n in &nums {
            if (!counter.contains_key(n)) {
                counter.insert(*n, 0);
            }
            counter.insert(*n, counter[n] + 1);
        }
        let mut counter_list: Vec<Vec<i32>> = Vec::new();
        for (key, value) in &counter {
            let mut to_append: Vec<i32> = Vec::new();
            to_append.push(*key);
            to_append.push(*value);
            counter_list.push(to_append);
        }
        counter_list.sort_by(|a, b| b[1].partial_cmp(&a[1]).unwrap());
        let mut res: Vec<i32> = Vec::new();
        for i in 0..k as usize {
            res.push(counter_list[i][0]);
        }
        return res;
    }
}
