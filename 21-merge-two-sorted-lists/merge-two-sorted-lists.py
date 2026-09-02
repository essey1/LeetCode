# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        list3 = []
        list3 = ListNode()
        cur = list3

        while i!=None or j!=None:
            if i!=None and j!=None:
                if i.val<=j.val:
                    cur.next = i
                    cur = cur.next
                    i = i.next
                else:
                    cur.next = j
                    cur = cur.next
                    j = j.next
            elif i==None and j!=None:
                cur.next = j
                cur = cur.next
                j = j.next
            elif i!=None and j==None:
                cur.next = i
                cur = cur.next
                i = i.next
        return list3.next

                 

        