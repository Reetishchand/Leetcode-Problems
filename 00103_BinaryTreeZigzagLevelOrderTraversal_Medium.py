'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
  Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
  Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100'''
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.lis=[]
        def trav(root,l):
            if root:
                try:
                    self.lis[l].append(root.val)
                except:
                    self.lis.append([root.val])
                
                trav(root.left,l+1)
                trav(root.right,l+1)
        trav(root,0)
        return self.lis
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        order = self.levelOrder(root)
        for i in range(len(order)):
            if i%2!=0:
                order[i]=order[i][::-1]
        return order
        
