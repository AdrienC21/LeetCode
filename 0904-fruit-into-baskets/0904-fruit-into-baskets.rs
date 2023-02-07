use std::cmp;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let n: i32 = fruits.len() as i32;
        if (n <= 2) {
            return fruits.len() as i32;
        }
        let mut max_fruits: i32 = 1;
        let mut tree1: i32 = fruits[0];
        let mut tree2: i32 = -1;
        let mut basket1: i32 = 1;
        let mut basket1_if_new: i32 = 1;  // count values in a row
        let mut basket2: i32 = 0;
        let mut basket2_if_new: i32 = 1;  // count values in a row
        for i in 1..n as usize {
            if ((fruits[i] != tree1) && (fruits[i] != tree2)) {
                if (fruits[i-1] == tree1) {  // replace tree2
                    basket2 = 1;
                    basket2_if_new = 1;
                    tree2 = fruits[i];
                    basket1 = basket1_if_new;
                }
                else {  // replace tree1
                    basket1 = 1;
                    basket1_if_new = 1;
                    tree1 = fruits[i];
                    basket2 = basket2_if_new;
                }
            }
            else {
                if (fruits[i] == tree1) {
                    basket1 += 1;
                    if (fruits[i-1] != tree1) {
                        basket1_if_new = 1;
                    }
                    else {
                        basket1_if_new += 1;
                    }
                }
                else {
                    basket2 += 1;
                    if (fruits[i-1] != tree2) {
                        basket2_if_new = 1;
                    }
                    else {
                        basket2_if_new += 1;
                    }
                }
            }
            // update the max
            max_fruits = cmp::max(max_fruits, basket1 + basket2);
        }
        return max_fruits;
    }
}