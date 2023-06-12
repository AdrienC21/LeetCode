impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if (nums.len() == 0) {
            let ranges: Vec<String> = Vec::new();
            return ranges;
        }
        let mut ranges: Vec<String> = Vec::new();
        let mut current_range: i32 = nums[0];
        let mut current_nb: i32 = nums[0];
        let n: i32 = nums.len() as i32;
        let arrow: String = String::from("->");
        for i in 1..n as usize {
            if (nums[i] == (current_nb + 1)) {
                current_nb += 1;
            }
            else {
                if (current_range == current_nb) {
                    let mut to_add: String = current_nb.to_string();
                    ranges.push(to_add);
                }
                else {
                    let mut to_add: String = current_range.to_string();
                    to_add.push_str(&arrow);
                    to_add.push_str(&(current_nb.to_string()));
                    ranges.push(to_add);
                }
                current_range = nums[i];
                current_nb = nums[i];
            }
        }
        if (current_range == current_nb) {
            let mut to_add: String = current_nb.to_string();
            ranges.push(to_add);
        }
        else {
            let mut to_add: String = current_range.to_string();
            to_add.push_str(&arrow);
            to_add.push_str(&(current_nb.to_string()));
            ranges.push(to_add);
        }
        
        return ranges;
    }
}
