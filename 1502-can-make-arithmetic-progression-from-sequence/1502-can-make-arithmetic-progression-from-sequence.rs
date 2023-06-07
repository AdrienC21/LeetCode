impl Solution {
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool {
        let mut arr2: Vec<i32> = Vec::from(arr);
        arr2.sort();
        let prog: i32 = arr2[1] - arr2[0];
        let n: i32 = arr2.len() as i32;
        for i in 2..n as usize {
            if ((arr2[i] - arr2[i-1]) != prog) {
                return false;
            }
        }
        return true;
    }
}
