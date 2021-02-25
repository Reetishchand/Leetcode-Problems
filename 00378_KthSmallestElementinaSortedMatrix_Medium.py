'''Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
  Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
  Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= -109
All the rows and columns of matrix are guaranteed to be sorted in non-degreasing order.
1 <= k <= n2'''
 
class Solution:
    def sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            L,R = arr[:mid],arr[mid:]
            self.sort(L)
            self.sort(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                
                #     j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
                
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
            
            
            
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis=[]
        m,n=len(matrix),len(matrix[0])
        span=0
        for i in range(0,m):
            for j in range(n):
                lis.append(matrix[i][j])
        self.sort(lis)
        print(lis)
        return lis[k-1]
