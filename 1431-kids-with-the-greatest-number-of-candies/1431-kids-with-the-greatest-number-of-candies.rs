impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let mut res: Vec<bool> = Vec::new();
        let m: i32 = *(candies.iter().max().unwrap());
        for c in &candies {
            if ((*c + extra_candies) >= m) {
                res.push(true);
            }
            else {
                res.push(false);
            }
        }
        return res;
    }
}
