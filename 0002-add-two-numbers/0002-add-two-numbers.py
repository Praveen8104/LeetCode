# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        n1=''
        n2=''
        while(temp1!=None):
            n1+=str(temp1.val)
            temp1=temp1.next
        while(temp2!=None):
            n2+=str(temp2.val)
            temp2=temp2.next
        n3=int(n1[::-1])+int(n2[::-1])
        s=str(n3)
        s=s[::-1]
        temp3 = ListNode(0)
        head  = temp3
        for i in range(len(s)):
            head.next=ListNode(int(s[i]))
            head = head.next
        return temp3.next
