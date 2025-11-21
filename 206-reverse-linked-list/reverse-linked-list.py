# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive method

        #base case
        if head == None or head.next == None:
            return head
        
        #recusrsive case
        rec_head = Solution.reverseList(self, head.next)

        head.next.next = head

        head.next = None

        return rec_head


        # # iterative method
        # cur1 = head
        # reverse = ListNode()
        # cur2 =  reverse
        # stack = []
        # while cur1:
        #     stack.append(cur1.val)
        #     cur1 = cur1.next
        # print(stack)
        # for i in range(len(stack)):
        #     cur2.next = ListNode(stack.pop())
        #     cur2 = cur2.next

        # return reverse.next