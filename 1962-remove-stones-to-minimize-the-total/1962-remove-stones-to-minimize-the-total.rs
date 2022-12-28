use std::collections::BinaryHeap;

impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        for p in &piles {
            heap.push(*p);
        }
        let mut stones: i32;
        for i in 0..k {
            stones = heap.pop().unwrap();
            stones -= (stones / 2);
            heap.push(stones);
        }
        let mut res: i32 = 0;
        for p in &heap {
            res += *p;
        }
        return res;
    }
}
