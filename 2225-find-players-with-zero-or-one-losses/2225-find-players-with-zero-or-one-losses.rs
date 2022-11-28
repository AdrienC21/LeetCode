use std::collections::HashSet;

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut players: HashSet<i32> = HashSet::new();
        let mut has_lost: HashSet<i32> = HashSet::new();
        let mut has_lost_twice: HashSet<i32> = HashSet::new();
        let mut w: i32;
        let mut l: i32;
        for m in &matches {
            w = m[0];
            l = m[1];
            players.insert(w);
            players.insert(l);
            if (has_lost.contains(&l)) {
                has_lost_twice.insert(l);
            }
            has_lost.insert(l);
        }
        let mut res1: Vec<i32> = Vec::new();
        for x in players.difference(&has_lost) {
            res1.push(*x);
        }
        res1.sort();
        let mut res2: Vec<i32> = Vec::new();
        for x in has_lost.difference(&has_lost_twice) {
            res2.push(*x);
        }
        res2.sort();
        let mut res: Vec<Vec<i32>> = Vec::new();
        res.push(res1);
        res.push(res2);
        return res;
    }
}
