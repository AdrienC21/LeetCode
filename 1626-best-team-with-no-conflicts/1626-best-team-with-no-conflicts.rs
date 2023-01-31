use std::cmp;
use std::cmp::Ordering;

fn custom_cmp(a: &Vec<i32>, b: &Vec<i32>) -> Ordering {
    if (a[0] < b[0]) {
        return Ordering::Less;
    } else if (a[0] > b[0]) {
        return Ordering::Greater;
    }
    if (a[1] < b[1]) {
        return Ordering::Less;
    } else if (a[1] > b[1]) {
        return Ordering::Greater;
    }
    return Ordering::Equal;
}

impl Solution {
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        let n: i32 = scores.len() as i32;
        let mut dp: Vec<i32> = Vec::new();
        // dp[i] max score of team that includes play i
        for i in 0..n {
            dp.push(0);
        }
        let mut L: Vec<Vec<i32>> = Vec::new();
        for i in 0..n as usize {
            let mut v: Vec<i32> = Vec::new();
            v.push(ages[i]);
            v.push(scores[i]);
            L.push(v);
        }
        L.sort_by(custom_cmp);  // sort by age first

        let mut score: i32;
        for i in 0..n as usize {
            score = L[i][1];
            dp[i] = score;
            for j in 0..i {
                if (score >= L[j][1]) {  // if a younger player has a higher score, try to include him
                    dp[i] = cmp::max(dp[i], dp[j] + score);
                }
            }
        }
        
        // return max of dp
        let mut max_dp: i32 = 0;
        for i in 0..n as usize {
            max_dp = cmp::max(max_dp, dp[i]);
        }
        return max_dp;
    }
}