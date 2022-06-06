# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iterative solution, time limit exceeded
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []
        lenA = 0
        lenB = 0
        iterateA = headA
        iterateB = headB
        while iterateA:
            stackA.append(iterateA)
            iterateA = iterateA.next
            lenA += 1
        while iterateB:
            stackB.append(iterateB)
            iterateB = iterateB.next
            lenB += 1
        common = 0  # number last values in common
        while stackA and stackB and (stackA.pop() == stackB.pop()):
            common += 1
        if not(common):
            return None
        skipA = lenA - common
        skipB = lenB - common
        if skipA < skipB:
            iterateA = headA
            while skipA:
                skipA -= 1
                iterateA = iterateA.next
            return iterateA
        iterateB = headB
        while skipB:
            skipB -= 1
            iterateB = iterateB.next
        return iterateB
        
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        to_compareA = headA
        while not(to_compareA is None):
            to_compareB = headB
            while to_compareB:
                if to_compareB == to_compareA:
                    return to_compareA
                to_compareB = to_compareB.next
            to_compareA = to_compareA.next
        return None
    """
