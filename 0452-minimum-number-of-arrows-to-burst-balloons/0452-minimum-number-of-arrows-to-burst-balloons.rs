impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut points_mut: Vec<Vec<i32>> = Vec::from(points);
        points_mut.sort_by(|a, b| a[1].cmp(&b[1]));  // sort by end
        let mut current_end: i32 = points_mut[0][1];
        let mut res: i32 = 1;  // number of arrows to shoot
        let mut start: i32;
        let mut end: i32;
        for p in &points_mut {
            start = p[0];
            end = p[1];
            if (start > current_end) {  // this balloons and the next ones will not be bursted by the last arrow
                current_end = end;
                res += 1;
            }
        }
        return res;
    }
}
