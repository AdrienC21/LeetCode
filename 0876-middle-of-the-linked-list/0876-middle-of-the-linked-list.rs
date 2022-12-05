// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut root = head.clone().unwrap();
        let mut length: i32 = 1;
        while (root.next.is_some()) {
            root = root.next.unwrap();
            length += 1;
        }
        let mut k: i32 = (length / 2);
        root = head.unwrap();
        while (k > 1) {
            k -= 1;
            root = root.next.unwrap();
        }
        if (k == 0) {
            return Some(root);
        }
        return root.next;  // last k
    }
}