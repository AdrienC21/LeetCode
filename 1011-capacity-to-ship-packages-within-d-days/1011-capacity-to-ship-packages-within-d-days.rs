impl Solution {
    pub fn run_simulation(weights: &Vec<i32>, days: i32, max_capacity: i32) -> bool {
        let mut day: i32 = 1;
        let mut running_sum: i32 = 0;
        let mut i: usize = 0;
        let n: usize = weights.len();
        while ((day <= days) & (i < n)) {
            if ((running_sum + weights[i]) > max_capacity) {  // new day
                day += 1;
                running_sum = 0;
            }
            else {  // update running_sum, process next package later
                running_sum += weights[i];
                i += 1;
            }
        }
        return (day <= days)  // if True, we shipped everyting on time
    }
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        if (days == 1) {
            return weights.iter().sum();
        }
        let mut i: i32 = *weights.iter().max().unwrap();  // minimum capacity to put all the packages
        let mut j: i32 = weights.iter().sum();  // maximum capacity (load everything in 1 day)
        let mut m: i32;
        while (i < (j - 1)) {
            m = i + (j - i) / 2;
            if (Solution::run_simulation(&weights, days, m)) {
                j = m;
            }
            else {
                i = m;
            }
        }
        while (!Solution::run_simulation(&weights, days, i)) {
            i += 1;
        }
        return i;
    }
}

