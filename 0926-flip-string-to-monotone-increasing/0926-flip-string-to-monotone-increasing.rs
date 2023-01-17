use std::cmp;

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let n: i32 = s.len() as i32;
        
        // binary string as a list of int
        let mut bs: Vec<i32> = Vec::new();
        let s_vec: Vec<char> = s.chars().collect();
        for x in &s_vec {
            bs.push(*x as i32 - 48);
        }
        
        // ones to flip to become 0 before index i
        let mut ones_to_flip: Vec<i32> = Vec::new();
        ones_to_flip.push(0);
        let mut running_sum: i32 = 0;
        for b in &bs {
            running_sum += *b;
            ones_to_flip.push(running_sum);
        }
        
        // zeros to flip to become 1 after index i
        // the list is reversed here
        let mut zeros_to_flip_reverse: Vec<i32> = Vec::new();
        zeros_to_flip_reverse.push(0);
        let b: i32;
        running_sum = 0;
        for b_i in 0..n {
            running_sum += (1 - (bs[((n - b_i) as usize) - 1] as i32));
            zeros_to_flip_reverse.push(running_sum);
        }

        // calculate the minimum
        let mut res: i32 = i32::MAX; 
        for i in 0..(n+1) {
            res = cmp::min(res, ones_to_flip[i as usize] + zeros_to_flip_reverse[(n-i) as usize]);
        }
        return res;
    }
}