'''Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
  Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
 '''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s,t)
    def traverse(self,s,t):
         return  s!=None and ( self.equals(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t))
    def equals(self,x,y):
        if(x==None and y==None):
            return True
        if(x==None or y==None):
            return False
        return x.val==y.val and self.equals(x.left,y.left) and self.equals(x.right,y.right)
        
        
