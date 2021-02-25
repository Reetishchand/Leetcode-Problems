'''Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.
  Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.
Example 2:
Input: heights = [5,1,2,3,4]
Output: 5
Example 3:
Input: heights = [1,2,3,4,5]
Output: 0
  Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100'''
 
class Solution:
   
    def heightChecker(self, heights: List[int]) -> int:
      # self.moves=0
        def merge(nums):
            if len(nums)>1:
                mid=len(nums)//2
                L,R=nums[:mid],nums[mid:]
                merge(L)
                merge(R)
                i,j,k=0,0,0
                while i<len(L) and j<len(R):
                    
                    if L[i]<R[j]:
                        
                        nums[k]=L[i]
                        i+=1
                    else:
                        
                        nums[k]=R[j]
                        j+=1
                    k+=1
                while i<len(L) :
                    nums[k]=L[i]
                    i+=1
                    k+=1
                while j<len(R) :
                    nums[k]=R[j]
                    j+=1
                    k+=1
            return nums
        new=heights[:]
        c=0
        merge(new)
        for i in range(len(heights)):
            if new[i]!=heights[i]:
                c+=1
       # print(new,heights)
        return c
        
