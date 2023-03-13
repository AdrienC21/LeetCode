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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let res: bool = match root {
            Some(node) => Solution::sym(node.borrow().left.clone(), node.borrow().right.clone()),
            _ => true,
        };
        return res;
    }
    pub fn check_sym_with_val(n1: Rc<RefCell<TreeNode>>, n2: Rc<RefCell<TreeNode>>) -> bool {
        if (n1.borrow().val != n2.borrow().val) {
            return false;
        }
        return (Solution::sym(n1.borrow().left.clone(), n2.borrow().right.clone()) && Solution::sym(n1.borrow().right.clone(), n2.borrow().left.clone()));
    }
    pub fn sym(r1: Option<Rc<RefCell<TreeNode>>>, r2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let res: bool = match (r1, r2) {
            (Some(n1), Some(n2)) => Solution::check_sym_with_val(n1, n2),
            (Some(n1), _) => false,
            (_, Some(n2)) => false,
            (_, _) => true,
        };
        return res;
    }
}
