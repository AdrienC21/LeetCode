use std::collections::HashSet;
impl Solution {
    pub fn is_left(p1: (i32,i32), p2: (i32,i32), m: (i32,i32)) -> bool {
        // (piM x pi pj).uz >= 0 if m to the right of segment pipj
        // x is vectorial product
        return ((p2.0-p1.0)*(m.1-p1.1)-(p2.1-p1.1)*(m.0-p1.0)) > 0;
    }
    pub fn outer_trees(mut trees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if (trees.len() == 1) {
            return trees;
        }
        let mut hull: Vec<(i32, i32)> = Vec::new();
        trees.sort_unstable_by_key(|item| (item[0], item[1]));;  // left to right, down to up if equality

        // lower hull: left to right
        for t in 0..trees.len() {
            let tree: (i32,i32) = (trees[t][0], trees[t][1]);
            while (hull.len() > 1) {
                if (Solution::is_left(hull[(hull.len() as usize)-1], hull[(hull.len() as usize)-2], tree)) {
                    hull.pop();
                }
                else {
                    break;
                }
            }
            hull.push(tree);
        }
        hull.pop();  // remove last duplicated element

        // upper hull: left to right
        for t in (0..trees.len()).rev() {
            let tree: (i32,i32) = (trees[t][0], trees[t][1]);
            while (hull.len() > 1) {
                if (Solution::is_left(hull[(hull.len() as usize)-1], hull[(hull.len() as usize)-2], tree)) {
                    hull.pop();
                }
                else {
                    break;
                }
            }
            hull.push(tree);
        }
        hull.pop();  // remove last duplicated element

        // remove duplcated element
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut set: HashSet<(i32,i32)> = HashSet::new();
        for i in 0..hull.len() {
            let tree: (i32,i32) = hull[i];
            if (!set.contains(&tree)) {
                set.insert(tree);
                let mut to_add: Vec<i32> = Vec::new();
                to_add.push(tree.0);
                to_add.push(tree.1);
                res.push(to_add);
            }
        }
        return res;
    }
}