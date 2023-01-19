impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut res: i32 = 0;
        let mut running_sum_mod: i32 = 0;
        let mut count: Vec<i32> = Vec::new();  // count the running sums per modulo
        count.push(1);
        for i in 0..(k-1) {
            count.push(0);
        }
        for n in &nums {
            running_sum_mod += *n;
            running_sum_mod = ((running_sum_mod % k) + k) % k;  // force value between 0 and k excluded
            res += count[running_sum_mod as usize];
            count[running_sum_mod as usize] += 1;
        }

        return res;
    }
}
