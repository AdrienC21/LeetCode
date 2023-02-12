use std::collections::HashMap;


impl Solution {
    pub fn ceil(a: f64) -> i64 {
        if ((a - ((a as i64) as f64)) > 0.0) {
            return (a as i64) + 1;
        }
        return a as i64;
    }
    pub fn recSearch(u: i32, parent: i32, seats: f64, graph: &mut HashMap<i32, Vec<i32>>, res: &mut i64) -> i64 {
        let mut u_passengers: i64 = 0;
        if graph.contains_key(&u) {
            let mut v: i32;
            let mut v_passengers: i64;
            for i_v in 0..(graph[&u].len()) as usize {
                v = graph[&u][i_v];
                if (v != parent) {
                    v_passengers = Solution::recSearch(v, u, seats, graph, res);
                    u_passengers += v_passengers;
                    *res += Solution::ceil((v_passengers as f64) / seats); // number of liters to cover the edge!
                }
            }
        }
        return u_passengers + 1;  // +1 for u;
    }
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut a: i32;
        let mut b: i32;
        for i in 0..(roads.len()) as usize {
            a = roads[i][0];
            b = roads[i][1];
            graph.entry(a)
                .or_insert_with(Vec::new)
                .push(b);
            graph.entry(b)
                .or_insert_with(Vec::new)
                .push(a);
        }
        let mut res: i64 = 0;
        
        let x: i64 = Solution::recSearch(0, -1, seats as f64, &mut graph, &mut res);
        return res;
    }
}