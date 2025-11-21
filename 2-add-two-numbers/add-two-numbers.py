# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
                       1
        2 -> 4 -> 8 -> 0
        5 -> 6 -> 4 -> 0
        7 -> 0 -> 3 -> 1

        traverse the linked lists
        if one linked list ends treat the values as 0
        keep track of the carry
        add a node if we need to add a digit

        carry = 0
        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            same with l2

            sum = v1+v2+carry
            if sum > 9:
                carry += 1
                sum = sum%10
            
            cur.val = sum
            cur = cur.next
        """

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            

            summ = v1+v2+carry
            carry = 0
            if summ > 9:
                carry += 1
                summ = summ%10
            
            cur.next = ListNode(summ)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            cur.next = ListNode(carry)
            cur = cur.next

        return dummy.next

        