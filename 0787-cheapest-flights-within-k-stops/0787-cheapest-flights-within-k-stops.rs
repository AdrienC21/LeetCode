use std::collections::HashMap;

impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        // distance vector and new_distance copy
        let mut distance: Vec<i64> = Vec::new();
        for i in 0..n {
            distance.push((i32::MAX) as i64);
        }
        distance[src as usize] = 0;
        let mut new_distance: Vec<i64>= Vec::new();
        for i in 0..n {
            new_distance.push(distance[i as usize]);
        }
        
        // Graph
        let mut graph: Vec<Vec<Vec<i64>>> = Vec::new();
        for u in 0..n {
            let mut vec: Vec<Vec<i64>> = Vec::new();
            graph.push(vec);
        }
        let mut u: i64;
        let mut v: i64;
        let mut p: i64;
        for i in 0..(flights.len() as i32) {
            u = flights[i as usize][0] as i64;
            v = flights[i as usize][1] as i64;
            p = flights[i as usize][2] as i64;
            let mut add_vec: Vec<i64> = Vec::new();
            add_vec.push(v);
            add_vec.push(p);
            graph[u as usize].push(add_vec);
        }
        
        // bellman-ford?
        for i in 0..(k+1) {
            for u in 0..n {
                for u_i in 0..(graph[u as usize].len() as i32) {
                    v = graph[u as usize][u_i as usize][0];
                    p = graph[u as usize][u_i as usize][1];
                    if ((distance[u as usize] + p) < new_distance[v as usize]) {
                        new_distance[v as usize] = distance[u as usize] + p
                    }
                }
            }
            // update distance
            for j in 0..n {
                distance[j as usize] = new_distance[j as usize];
            }
        }
        if (distance[dst as usize] == ((i32::MAX) as i64)) {
            return -1;
        }
        return distance[dst as usize] as i32;
    }
}