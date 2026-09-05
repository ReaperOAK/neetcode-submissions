# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d=ListNode(0,head)
        gP=d
        while True:
            kth=self.getKth(gP,k)
            if not kth:
                break
            gN=kth.next

            p,c=kth.next,gP.next
            while c!=gN:
                tmp=c.next
                c.next=p
                p=c
                c=tmp
            
            tmp=gP.next
            gP.next=kth
            gP=tmp
        return d.next


    def getKth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr