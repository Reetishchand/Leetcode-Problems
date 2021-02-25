'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''
 
class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(arr)<2:
            return arr
        z=0
        for i in range(len(arr)):
            if  arr[i]==0:
                z=i
                while  z<len(arr) and arr[z]==0 :
                    z+=1  
                if z>i and z<len(arr):
                    arr[i],arr[z]=arr[z],arr[i]
                
                    
                
                

