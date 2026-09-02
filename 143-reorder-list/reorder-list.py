# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        temp = head.next
        head.next = tail
        tail.next = temp
        maybe do this recursively
        """
        s=head
        f=head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        s.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            temp = first.next
            temp2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2
