'''Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)'''
 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        F,B,res = [0]*l,[0]*l,[0]*l
        F[0]=nums[0]
        B[-1]=nums[-1]
        for i in range(1,l):
            F[i]=nums[i]*F[i-1]
        for i in range(l-2,0,-1):
            B[i]=B[i+1]*nums[i]
        res[0]=B[1]
        res[-1]=F[-2]
        for i in range(1,l-1):
            res[i] = F[i-1]*B[i+1]
        return res
