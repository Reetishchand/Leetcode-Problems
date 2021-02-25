'''Given the head of a linked list, rotate the list to the right by k places.
  Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
  Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109'''
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return
        h=head
        l=1
        while h.next!=None:
            h=h.next
            l+=1
        
        h.next=head
        h=head
        
        if k>=l:
            k=k%l
        k=l-k
        while k>1:
            k-=1
            head=head.next
        print(head.val)
        h=head
        head=head.next
        h.next=None
        return head
        
