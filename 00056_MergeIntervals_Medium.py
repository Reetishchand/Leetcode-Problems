'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
  Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
  Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104'''
 
class Solution:
    
    def sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            L,R = arr[:mid],arr[mid:]
            self.merge(L)
            self.merge(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if L[i][0]<R[j][0] or (L[i][0]==R[j][0] and  L[i][1]<R[j][1]):
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1
            
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
            
                
    
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        self.sort(arr)
        i=1
        res=[]
        res.append(arr[0])
        while i<len(arr):
            if res[-1][1]>=arr[i][0] and res[-1][1]<arr[i][1]:
                    x=res.pop()
                    res.append([x[0],arr[i][1]])
            elif res[-1][1]>=arr[i][0] and res[-1][1]>=arr[i][1]:
                i+=1
                continue
            else:
                res.append(arr[i])
            i+=1
        return res
                
        
