# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        c=0
        while cur:
            c+=1
            cur=cur.next
        n=c-n
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        cur=head
        c=0
        while c<n:
            prev=cur
            cur=cur.next
            c+=1
        prev.next=cur.next
        return dummy.next