'''Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
Example:
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
  Note:
There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/'''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.lis=[]
        def inorder(root):
            if root:
                inorder(root.left)
                self.lis.append(root.val)
                inorder(root.right)
        inorder(root)
        ans=float("inf")
        for i in range(1,len(self.lis)):
            ans=min(ans,self.lis[i]-self.lis[i-1])
        return ans
