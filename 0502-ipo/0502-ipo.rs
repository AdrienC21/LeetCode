use std::collections::BinaryHeap;

impl Solution {
    // Use heap for maximum efficiency
    // Rust implementation mine, pseudo code not mine. I wanted to do DP initially ...
    pub fn find_maximized_capital(k: i32, w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        let mut profits_candidate = BinaryHeap::new();
        let mut projects = BinaryHeap::new();
        // sort by lowest capital first!
        for i in 0..(profits.len()) as usize {
            projects.push((-capital[i], -profits[i]));
        }
        let mut total_capital: i32 = w;
        let mut sent: bool;
        let mut c: i32;
        let mut p: i32;
        for i in 0..k {
            sent = (!projects.is_empty());
            if (sent) {
                sent = (-(*projects.peek().unwrap()).0 <= total_capital);
            }
            while (sent) {  // we can afford this project
                let tup: (i32, i32) = projects.pop().unwrap();
                c = -tup.0;
                p = -tup.1;
                profits_candidate.push(p);
                // update sentinelle variable
                sent = (!projects.is_empty());
                if (sent) {
                    sent = (-(*projects.peek().unwrap()).0 <= total_capital);
                }
            }
            if (profits_candidate.is_empty()) {  // no candidate to pull, end of the pre-IPO
                break;
            }
            // else, increase capital by taking the biggest profit project available
            p = profits_candidate.pop().unwrap();
            total_capital += p
        }
        return total_capital;
    }
}