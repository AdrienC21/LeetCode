impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let mut min_salary: i32 = i32::MAX;
        let mut max_salary: i32 = 0;
        let mut cum_sum: f64 = 0.0;
        let mut nb_employees = salary.len() as f64;
        let mut s: i32;
        for i in 0..nb_employees as usize {
            s = salary[i];
            cum_sum = cum_sum + (s as f64);
            if (s < min_salary) {
                min_salary = s;
            }
            if (s > max_salary) {
                max_salary = s;
            }
        }
        cum_sum = cum_sum - (min_salary as f64);
        cum_sum = cum_sum - (max_salary as f64);
        nb_employees = nb_employees - 2.0;
        return cum_sum / nb_employees;
    }
}
