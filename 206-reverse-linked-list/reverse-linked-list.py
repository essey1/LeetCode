# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # construct an array and remove from the top (LIFO)
        # 2nd option recursively, recursively visit until you get to last and unwind the recursive stack, still LIFO
        
        #base case
        if head == None or head.next == None:
            return head

        #recursive case
        recHead = Solution.reverseList(self, head.next)

        head.next.next = head

        head.next = None

        return recHead



        