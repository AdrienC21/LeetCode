impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let n: i32 = arr.len() as i32;
        let mut i: usize = 0;
        let mut j: usize = (n as usize) - 1;
        let mut m: usize;
        while (i < j) {
            m = i + (j - i) / 2;
            if (arr[m] < arr[m+1]) {
                i = m + 1;
            }
            else if (arr[m] < arr[m-1]) {
                j = m - 1;
            }
            else {
                return m as i32;
            }
        }
        return i as i32;
    }
}
