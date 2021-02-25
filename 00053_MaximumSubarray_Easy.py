'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
  Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
Input: nums = [1]
Output: 1
Example 3:
Input: nums = [0]
Output: 0
Example 4:
Input: nums = [-1]
Output: -1
Example 5:
Input: nums = [-100000]
Output: -100000
  Constraints:
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
  Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.'''
 
class Solution:
    def crossSum(self,nums,l,h,mid):
        ls=rs = -9999999999999
        c=0
        for i in range(mid+1,h+1):
            c+=nums[i]
            ls=max(ls,c)
        c=0
        for i in range(mid,l-1,-1):
            c+=nums[i]
            rs=max(rs,c)
        return ls+rs
            
    def helper(self,nums,l,h):
        if l==h:
            return nums[l]
        mid = (l+h)//2
        ls=self.helper(nums,l,mid)
        rs=self.helper(nums,mid+1,h)
        cs = self.crossSum(nums,l,h,mid)
        
        return max(max(ls,rs),cs)
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums,0,len(nums)-1)
        
