'''Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ? k ? array's length.'''
 
class Solution:
    def merge(self,arr):
        if len(arr)>1:
            mid = len(arr)//2
            L,R = arr[:mid],arr[mid:]
            self.merge(L)
            self.merge(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
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
        return arr
            
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.merge(nums)
        print(nums)
        return nums[-k]
        
