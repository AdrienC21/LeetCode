impl Solution {
    pub fn fib(n: i32) -> i32 {
        let five = 5 as f32;
        let sqrt5 = five.sqrt();
        let phi = (1 as f32 + sqrt5) / (2 as f32);
        let res = (f32::powf(phi, n as f32) / sqrt5).round();
        return res as i32;
    }
}