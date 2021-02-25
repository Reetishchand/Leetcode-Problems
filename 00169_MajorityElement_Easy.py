'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ?n / 2? times. You may assume that the majority element always exists in the array.
  Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
  Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
  Follow-up: Could you solve the problem in linear time and in O(1) space?'''
 
class Solution:
    def countInRange(self,nums,num,lo,hi):
        c=0
        for i in range(lo,hi+1):
            if nums[i]==num:
                c+=1
        return c
        
    def divAndConq(self,nums,lo,hi):
        if lo==hi:
            return nums[lo]
        
        mid = (hi-lo)//2 + lo
        left = self.divAndConq(nums,lo,mid)
        print("left",left)
        right = self.divAndConq(nums,mid+1,hi)
        print("right",right)

        if left==right:
            return left

        lc = self.countInRange(nums,left,lo,hi)
        rc = self.countInRange(nums,right,lo,hi)
        if lc>rc:
            return left
        return right
            
            
            
    
    def majorityElement(self, nums: List[int]) -> int:
        return self.divAndConq(nums,0,len(nums)-1)
        
        
