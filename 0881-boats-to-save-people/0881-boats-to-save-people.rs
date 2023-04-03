impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let mut people_sorted: Vec<i32> = Vec::from(people);
        people_sorted.sort();
        let mut res: i32 = 0;
        let n: i32 = people_sorted.len() as i32;
        let mut i: i32 = 0;
        let mut j: i32 = n - 1;
        while (i <= j) {
            if ((people_sorted[j as usize] + people_sorted[i as usize]) <= limit) {
                i += 1;
            }
            j -= 1;
            res += 1;
        }
        return res;
    }
}
