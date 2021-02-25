'''Given an m x n matrix, return all elements of the matrix in spiral order.
  Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
  Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''
 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return 
        r2,c2 = len(matrix)-1,len(matrix[0])-1
        ans=[]
        r1,c1=0,0
        while r1<=r2 and c1<=c2:
            for i in range(c1,c2+1):
                print(matrix[r1][i])
                ans.append(matrix[r1][i])
            for i in range(r1+1,r2+1):
                print(matrix[i][c2])
                ans.append(matrix[i][c2])
            if r1<r2 and c1<c2:
                for i in range(c2-1,c1-1,-1):
                    print(matrix[r2][i])
                    ans.append(matrix[r2][i])
                for i in range(r2-1,r1,-1):
                    print(matrix[i][c1])
                    ans.append(matrix[i][c1])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return ans
                
        
