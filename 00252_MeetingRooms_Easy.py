'''Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
  Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
  Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106'''
 
class Solution:
    def merge(self,nums):
        if len(nums)>1:
            mid = len(nums)//2
            L,R = nums[:mid],nums[mid:]
            self.merge(L)
            self.merge(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if L[i][0]<R[j][0]:
                    nums[k]=L[i]
                    i+=1
                else:
                    nums[k]=R[j]
                    j+=1
                k+=1
            
            while i<len(L):
                nums[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                nums[k]=R[j]
                j+=1
                k+=1
            return nums
            
            
    def canAttendMeetings(self, arr: List[List[int]]) -> bool:
        self.merge(arr)
        print(arr)
        for i in range(1,len(arr)):
            cur,prev = arr[i],arr[i-1]
            if not (cur[0]>=prev[0] and cur[0]>=prev[1]):
                return False
        
        return True
