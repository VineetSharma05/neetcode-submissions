# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        head1=None
        while cur:
            new=ListNode(cur.val)
            if head1==None:
                head1=new
            else:
                new.next=head1
                head1=new
            head=head.next
            cur=cur.next
        return head1

        
        