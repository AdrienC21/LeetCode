impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        let mut count: i32 = 0;
        let mut current_nb: i32 = 1;
        let mut i: usize = 0;  // pointer in arr
        let n: usize = arr.len() as usize;
        while (i < n) {
            if (arr[i] != current_nb) {
                count += 1;
                if (count == k) {
                    return current_nb;
                }
            }
            else {
                i += 1;
            }
            current_nb += 1;
        }
        return current_nb + (k - count - 1);
    }
}