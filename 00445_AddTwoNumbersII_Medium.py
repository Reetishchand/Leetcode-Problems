'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7'''
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def prepNum(self,node):
        n=0
        while node!=None:
            n=(n*10)+node.val
            node=node.next
        return n
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.prepNum(l1)
        n2 = self.prepNum(l2)
        print(n1,n2)
        n = str(n1+n2)
        ans=ListNode(-1)
        head=ans
        for i in n:
            ans.next=ListNode(int(i))
            ans=ans.next
        return head.next
            
            
        
