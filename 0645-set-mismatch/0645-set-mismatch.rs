use std::collections::HashSet;
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut s: HashSet<i32> = HashSet::new();;
        let mut res = vec![0, 0];
        for i in 0..nums.len() as i32 {
            let num: i32 = nums[i as usize];
            if (s.contains(&num)) {  // in double
                res[0] = num;
            }
            s.insert(num);
        }
        for i in 1..(nums.len()+1) as i32 {
            if (!(s.contains(&i))) {  // missing
                res[1] = i;
                break;
            }
        }
        return res;
    }
}