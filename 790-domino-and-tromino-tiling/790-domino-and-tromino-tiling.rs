use std::collections::HashMap;

impl Solution {
    fn rec1(n: i64, mut cache1: &mut HashMap<i64, i64>, mut cache2: &mut HashMap<i64, i64>, m: i64) -> i64 {
        if (cache1.contains_key(&n)) {
            return cache1[&n];
        }
        let mut res: i64 = 0;
        res += Solution::rec1(n-1, cache1, cache2, m);
        res %= m;
        res += Solution::rec1(n-2, cache1, cache2, m);
        res %= m;
        let a: i64 = Solution::rec2(n-1, cache1, cache2, m);
        res += a;
        res %= m;
        res += a;
        res %= m;
        cache1.insert(n, res);
        return res;
    }
    fn rec2(n: i64, mut cache1: &mut HashMap<i64, i64>, mut cache2: &mut HashMap<i64, i64>, m: i64) -> i64 {
        if (cache2.contains_key(&n)) {
            return cache2[&n];
        }
        let mut res: i64 = 0;
        res += Solution::rec2(n-1, cache1, cache2, m);
        res %= m;
        res += Solution::rec1(n-2, cache1, cache2, m);
        res %= m;
        cache2.insert(n, res);
        return res;
    }
    pub fn num_tilings(n: i32) -> i32 {
        let mut cache1: HashMap<i64, i64> = HashMap::new();
        cache1.insert(0, 0);
        cache1.insert(1, 1);
        cache1.insert(2, 2);
        let mut cache2: HashMap<i64, i64> = HashMap::new();
        cache2.insert(0, 0);
        cache2.insert(1, 0);
        cache2.insert(2, 1);
        let m: i64 = (10_i64.pow(9) + 7) as i64;
        return Solution::rec1(n as i64, &mut cache1, &mut cache2, m) as i32;
    }
}
      
