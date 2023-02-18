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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if (root.is_some()) {
            let node = root.unwrap();
            let new_left: Option<Rc<RefCell<TreeNode>>> = Solution::invert_tree(node.borrow().right.clone());
            let new_right: Option<Rc<RefCell<TreeNode>>> = Solution::invert_tree(node.borrow().left.clone());
            let new_val: i32 = node.borrow().val;
            let res: Option<Rc<RefCell<TreeNode>>> = Some(Rc::new(RefCell::new(TreeNode {
                val: new_val,
                left: new_left,
                right: new_right
            })));
            return res;
        }
        return root;
    }
}
