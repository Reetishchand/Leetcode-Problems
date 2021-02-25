'''Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
  Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
  Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
  Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?'''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 
        self.ind = 0
        self.ans = -1
        
        def trav(root):
            if root:
                trav(root.left)
                self.ind+=1
                if self.ind==k:
                    self.ans=root.val
                    return 
                trav(root.right)
                
        trav(root)
        return self.ans
        
