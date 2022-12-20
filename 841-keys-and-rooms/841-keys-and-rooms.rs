use std::collections::HashSet;

impl Solution {
    pub fn visit(room: i32, mut seen: HashSet<i32>, rooms: Vec<Vec<i32>>) -> HashSet<i32> {
        if (!seen.contains(&room)) {
            seen.insert(room);
            let number_keys: i32 = rooms[room as usize].len() as i32;
            for i in 0..number_keys as usize {
                seen = Solution::visit(rooms[room as usize][i], seen, rooms.clone());
            }
        }
        return seen;
    }
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let n: i32 = rooms.len() as i32;
        let mut seen: HashSet<i32> = HashSet::new();
        
        seen = Solution::visit(0, seen, rooms);
        return ((seen.len() as i32) == n)
    }
}
