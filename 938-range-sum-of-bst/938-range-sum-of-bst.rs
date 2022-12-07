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
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        let r: i32 = match root {
            None => 0,
            Some(node) => {
                let mut res: i32 = 0;
                let node = node.borrow();
                if ((node.val >= low) & (node.val <= high)) {
                    res += node.val;
                }
                res += Solution::range_sum_bst(node.left.clone(), low, high);
                res += Solution::range_sum_bst(node.right.clone(), low, high);
                return res;
                },
        };
        return r;
    }
}
