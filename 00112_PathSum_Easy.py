'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
  Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:
Input: root = [1,2], targetSum = 0
Output: false
  Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000'''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,prev,s):
        if root and (root.left or root.right):
            return self.check(root.left,prev+root.val,s) or self.check(root.right,prev+root.val,s)
        elif root:
            return root.val+prev==s
        
            
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.check(root,0,sum)
