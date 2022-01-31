"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807."""

"""https://leetcode.com/problems/add-two-numbers/"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry =0
        Head=None
        temp=None
        while(l1 != None or l2 != None):
            v1=0
            v2=0
            if(l1!=None):
                v1=l1.val
                l1=l1.next
            if(l2!=None):
                v2=l2.val
                l2=l2.next
            sum=v1+v2+carry
            
            
            if(sum>9):
                # print(sum)
                carry=sum//10
                sum=sum%10
            else:
                carry=0
            if(Head==None):
                # print(sum,carry)
                Head=ListNode(sum)
                temp=Head
            else:
                node=ListNode(sum)
                temp.next=node
                temp=node
        
        if(carry!=0):
            node=ListNode(carry)
            temp.next=node
        return Head
            