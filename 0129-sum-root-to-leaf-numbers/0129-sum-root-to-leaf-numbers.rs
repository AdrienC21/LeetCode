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
    pub fn rec_search(root: Option<Rc<RefCell<TreeNode>>>, current_nb: i32, res: &mut i32) -> Option<i32> {
        if (!root.is_some()) {
            return None;
        }
        let node: Rc<RefCell<TreeNode>> = root.unwrap();
        let new_nb: i32 = 10 * current_nb + node.borrow().val;
        if (!node.borrow().left.clone().is_some() && !node.borrow().right.clone().is_some()) {
            *res += new_nb;
            return None;
        }
        if (!node.borrow().left.clone().is_some()) {
            Solution::rec_search(node.borrow().right.clone(), new_nb, res);
            return None;
        }
        if (!node.borrow().right.clone().is_some()) {
            Solution::rec_search(node.borrow().left.clone(), new_nb, res);
            return None;
        }
        Solution::rec_search(node.borrow().left.clone(), new_nb, res);
        Solution::rec_search(node.borrow().right.clone(), new_nb, res);
        return None;
    }
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res: i32 = 0;
        Solution::rec_search(root, 0, &mut res);
        return res;
    }
}