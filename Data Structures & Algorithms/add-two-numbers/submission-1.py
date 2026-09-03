# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        e1=0
        e2=0
        c=0
        while l1:
            e1=e1+l1.val*(10**c)
            c+=1
            l1=l1.next
        c=0
        while l2:
            e2=e2+l2.val*(10**c)
            c+=1
            l2=l2.next
        s=e1+e2
        dummy=ListNode()
        cur=dummy
        if s==0:
            dummy.next=ListNode(0)
        while s>0:
            new=ListNode(s%10)
            s=s//10
            cur.next=new
            cur=cur.next
        
        return dummy.next
                
        