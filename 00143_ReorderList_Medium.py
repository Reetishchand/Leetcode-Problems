'''Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.'''
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        if head is None:
            return
        cur= head
        st=[]
        while cur!=None:
            temp = cur
            st.append(temp)
            cur=cur.next
        cur=head
        f,r=0,len(st)-1
        i=1
        while f<r:
            if i%2!=0:
                st[f].next=st[r]
                f+=1
            else:
                st[r].next=st[f]
                r-=1
            i+=1
        st[f].next=None
