use std::collections::VecDeque;
use std::collections::HashSet;
impl Solution {
    pub fn add_tuple(u: (i32, i32), v: (i32, i32)) -> (i32, i32) {
        return (u.0 + v.0, u.1 + v.1);
    }
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let m: i32 = maze.len() as i32;
        let n: i32 = maze[0].len() as i32;
        let mut d: VecDeque<(i32, i32)> = VecDeque::new();
        d.push_back((entrance[0], entrance[1]));
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        seen.insert((entrance[0], entrance[1]));
        let mut res: i32 = 0;
        let directions: Vec<(i32, i32)> = Vec::from([(1, 0), (0, 1), (-1, 0), (0, -1)]);
        
        // variables
        let mut t: (i32, i32);
        let mut t2: (i32, i32);
        let mut x2: i32;
        let mut y2: i32;
        
        while (!d.is_empty()) {
            res += 1;
            let size_d: i32 = d.len() as i32;
            for i in 0..size_d {  // process the entire deque at time t
                t = d.pop_front().unwrap();
                // add unseen cells for t+1
                for k in &directions {
                    t2 = Solution::add_tuple(t, *k);
                    x2 = t2.0;
                    y2 = t2.1;
                    if ((x2 >= 0) & (x2 < m) & (y2 >= 0) & (y2 < n)) {
                        if (!seen.contains(&t2) & (maze[x2 as usize][y2 as usize] == '.')) {
                            if ((x2 == 0) || (x2 == (m-1)) || (y2 == 0) || (y2 == (n-1))) {
                                return res;
                            }
                            d.push_back(t2);
                            seen.insert(t2);
                        }
                    }
                }
            }
        }
        return -1;
    }
}