impl Solution {
    pub fn sign(n: i32) -> i32 {
        if (n > 0) {
            return 1;
        }
        return -1;
    }
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        let mut last_direction: i32 = 0;  // 1 or -1
        let mut i: usize = 0;
        let n: usize = asteroids.len();
        let mut ast: i32;
        let mut sign_ast: i32;
        let mut top_ast: i32;
        let mut not_append_ast: bool;
        while (i < n) {
            ast = asteroids[i];
            sign_ast = Solution::sign(ast);
            if ((last_direction == 1) & (sign_ast == -1)) {  // collision(s)
                not_append_ast = true;
                while (!res.is_empty()) {
                    top_ast = res.pop().unwrap();
                    if (top_ast < 0) {  // no more collision
                        res.push(top_ast);
                        not_append_ast = false;
                        break;
                    }
                    if (top_ast < (-ast)) {  // collision right win
                        not_append_ast = false;
                        continue;
                    }
                    if (top_ast == (-ast)) {  // two destroyed
                        not_append_ast = true;
                        break;
                    }
                    else {  // collision left win
                        res.push(top_ast);
                        not_append_ast = true;
                        break;
                    }
                }
                if (!(not_append_ast)) {
                    res.push(ast);
                }
            }
            else {  // no collision
                res.push(ast);
            }
            if (!res.is_empty()) {
                last_direction = Solution::sign(res[res.len()-1]);
            }
            else {
                last_direction = 0;
            }
            i += 1
        }
        return res;
    }
}
