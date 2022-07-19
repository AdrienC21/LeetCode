impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut pascal: Vec<Vec<i32>> = Vec::new();
        for i in 1..(num_rows+1) {
            let mut vect: Vec<i32> = Vec::new();
            for j in 0..i {
                vect.push(1);
            }
            pascal.push(vect);
        }
        for i in 1..num_rows as usize {
            for j in 1..i {
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1];
            }
        }
        return pascal;
    }
}
