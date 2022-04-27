# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.next is None:
            if list1.val <= list2.val:
                return ListNode(val=list1.val, next=list2)
            else:
                return ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))
        elif list2.next is None:
            if list2.val <= list1.val:
                return ListNode(val=list2.val, next=list1)
            else:
                return ListNode(val=list1.val, next=self.mergeTwoLists(list2, list1.next))
        else:
            if list1.val <= list2.val:
                return ListNode(val=list1.val, next=self.mergeTwoLists(list1.next, list2))
            else:
                return ListNode(val=list2.val, next=self.mergeTwoLists(list2.next, list1))