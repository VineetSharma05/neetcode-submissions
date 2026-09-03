# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        while temp is not None and temp.next is not None:
            cur = temp
            prev = None
            # Find last node
            while cur.next is not None:
                prev = cur
                cur = cur.next
            # Remove last node
            prev.next = None
            # Insert last node after temp
            cur.next = temp.next
            temp.next = cur
            # Move temp forward
            temp = cur.next
                
        