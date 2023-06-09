impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let n: i32 = letters.len() as i32;
        let mut i: i32 = 0;
        let mut j: i32 = n - 1;
        let mut m: i32;
        while (i < j) {
            m = i + (j - i) / 2;
            if (letters[m as usize] <= target) {
                i = m + 1;
            }
            else {
                j = m - 1;
            }
        }
        if (letters[i as usize] > target) {
            return letters[i as usize];
        }
        if (i < (n - 1)) {
            if (letters[(i+1) as usize] > target) {
                return letters[(i+1) as usize];
            }
        }
        return letters[0];
    }
}
