use std::collections::HashMap;


impl Solution {
    pub fn recSearch(n: i32, cache: &mut HashMap<i32, i32>) -> i32 {
        if (cache.contains_key(&n)) {
            return cache[&n];
        }
        let res: i32 = Solution::recSearch(n-1, cache) + Solution::recSearch(n-2, cache) + Solution::recSearch(n-3, cache);
        cache.insert(n, res);
        return res;
    }
    pub fn tribonacci(n: i32) -> i32 {
        let mut cache: HashMap<i32, i32> = HashMap::new();
        cache.insert(0, 0);
        cache.insert(1, 1);
        cache.insert(2, 1);
        return Solution::recSearch(n, &mut cache);
    }
}
