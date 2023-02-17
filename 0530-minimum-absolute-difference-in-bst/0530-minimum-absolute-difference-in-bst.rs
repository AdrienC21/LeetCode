// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn rec_search(root: Option<Rc<RefCell<TreeNode>>>, values: &mut Vec<i32>) -> () {
        if (root.is_some()) {
            let node: Rc<RefCell<TreeNode>> = root.unwrap();
            values.push(node.borrow().val);
            Solution::rec_search(node.borrow().left.clone(), values);
            Solution::rec_search(node.borrow().right.clone(), values);
        }
    }
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut values: Vec<i32> = Vec::new();

        Solution::rec_search(root, &mut values);
        values.sort();
        let mut res: i32 = i32::MAX;
        for i in 0..(values.len()-1) as usize {
            if ((values[i+1] - values[i]) < res) {
                res = values[i+1] - values[i];
            }
        }
        return res;
    }
}