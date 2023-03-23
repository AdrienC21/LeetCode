use std::collections::HashSet;
use std::collections::HashMap;

impl Solution {
    pub fn dfs(i: i32, graph: &HashMap<i32, Vec<i32>>, visited: &mut HashSet<i32>) {
        let mut to_visit: Vec<i32> = Vec::new();
        to_visit.push(i);
        let mut u: i32;
        while (!to_visit.is_empty()) {
            u = to_visit.pop().unwrap();
            visited.insert(u);
            if (graph.contains_key(&u)) {
                for v in &graph[&u] {
                    if (!visited.contains(&v)) {
                        to_visit.push(*v);
                    }
                }
            }
        }
    }
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        if ((connections.len() as i32) < (n - 1)) {  // we need at least n-1 connections to connect n computers
            return -1;
        }
        // we need to connect connex components of the graph
        // find the components with DFS
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut a: i32;
        let mut b: i32;
        for i in 0..(connections.len() as i32) as usize {
            a = connections[i][0];
            b = connections[i][1];
            graph.entry(a).or_insert_with(Vec::new).push(b);
            graph.entry(b).or_insert_with(Vec::new).push(a);
        }
        let mut visited: HashSet<i32> = HashSet::new();         
        let mut nb_components: i32 = 0;
        for i in 0..n {
            if (!visited.contains(&i)) {
                nb_components += 1;
                Solution::dfs(i, &graph, &mut visited);
            }
        }
        return nb_components - 1;
    }
}