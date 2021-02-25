'''Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
  Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
  Note:
The total number of elements of the given matrix will not exceed 10,000.'''
 
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dic={}
        arr=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                try:
                    dic[i+j].append(matrix[i][j])
                except:
                    dic[i+j] = [matrix[i][j]]
        for i in dic.keys():
            if i%2==0:
                for j in dic[i][::-1]:
                    arr.append(j)
            else:
                for j in dic[i]:
                    arr.append(j)
        return arr
