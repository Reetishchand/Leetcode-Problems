'''Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
  Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
  Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100'''
 
class Solution:
    
    def subSet(self,nums,w,n):
        if w==0 and n==0:
            return True
        t = [[0 for i in range(w + 1)] for j in range(n + 1)]
        
        for i in range(n+1):
            t[i][0]=True
        
        for i in range(1,w+1):
            t[0][i]=False
        
        for i in range(1,n+1):
            for j in range(1,w+1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j - nums[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[n][w]
        
        
    
    
    def canPartition(self, nums: List[int]) -> bool:
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        if s%2!=0:
            return False
        return self.subSet(nums,s//2,len(nums))
        
        
