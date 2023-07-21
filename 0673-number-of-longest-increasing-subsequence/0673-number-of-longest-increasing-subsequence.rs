impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let n: i32 = nums.len() as i32;
        let mut dp_seq: Vec<i32> = Vec::new();
        let mut dp_count: Vec<i32> = Vec::new();  // dp store counts
        for i in 0..n {
            dp_seq.push(1);
            dp_count.push(1);
        }
        let mut num: i32;
        for i in 0..n as usize {
            num = nums[i];
            for j in 0..(i as i32) as usize {
                if (nums[i] > nums[j]) {  // increasing seq
                    if ((dp_seq[j] + 1) == dp_seq[i]) {
                        dp_count[i] += dp_count[j];
                    }
                    else if ((dp_seq[j] + 1) > dp_seq[i]) {  // update largest sequence
                        dp_count[i] = dp_count[j];
                        dp_seq[i] = dp_seq[j] + 1;
                    }
                }
            }
        }
        // Longest Increasing Subsequence
        let lis: i32 = *dp_seq.iter().max().unwrap();

        // Count of lis
        let mut res: i32 = 0;

        // Iterate over the lists
        let mut seq: i32;
        let mut count: i32;
        for i in 0..n as usize {
            seq = dp_seq[i];
            count = dp_count[i];
            if (seq == lis) {
                res += count;
            }
        }
        return res;
    }
}
