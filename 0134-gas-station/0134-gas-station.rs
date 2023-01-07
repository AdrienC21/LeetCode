impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let cost_sum: i32 = cost.iter().sum();
        let gas_sum: i32 = gas.iter().sum();
        if (cost_sum > gas_sum) {
            return -1;
        }
        // else: a solution exists
        let n: i32 = gas.len() as i32;
        let mut gas_tank: i32 = 0;
        let mut res: i32 = 0;
        for i in 0..n as usize {
            gas_tank += (-cost[i] + gas[i]);
            if (gas_tank < 0) {  // res can't be the initial start
                gas_tank = 0;  // empty gas tank
                res = (i as i32) + 1;  // test if an issue occur starting from i + 1
            }
        }
        return res;
    }
}
