impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let mut res: i32 = 0;
        let n: i32 = mat.len() as i32;
        for i in 0..n as usize {
            res += mat[i][i] + mat[i][(n as usize)-i-1];
        }
        if ((n % 2) == 1) {
            let a: usize = (n / 2) as usize;
            res -= mat[a][a];
        }
        return res;
    }
}
