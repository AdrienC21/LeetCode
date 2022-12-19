use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        if (source == destination) {
            return true;
        }
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for edge in &edges {
            graph.entry(edge[0]).or_insert(Vec::new()).push(edge[1]);
            graph.entry(edge[1]).or_insert(Vec::new()).push(edge[0]);
        }
        let mut seen: HashSet<i32> = HashSet::new();
        let mut to_visit: Vec<i32> = Vec::new();
        to_visit.push(source);
        let mut u: i32 = 0;
        while (!to_visit.is_empty()) {
            u = to_visit.pop().unwrap();
            if (!seen.contains(&u)) {
                seen.insert(u);
                for v in &graph[&u] {
                    if (*v == destination) {
                        return true;
                    }
                    if (!seen.contains(v)) {
                        to_visit.push(*v);
                    }
                }
            }
        }
        return false;
    }
}
