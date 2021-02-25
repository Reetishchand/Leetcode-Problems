'''You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.
  Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:
Input: arrays = [[1],[1]]
Output: 0
Example 3:
Input: arrays = [[1],[2]]
Output: 1
Example 4:
Input: arrays = [[1,4],[0,5]]
Output: 4
  Constraints:
m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.'''
 
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m,n=999999999,-9999999999
        mm,nn=-1,-1
        for i in range(len(arrays)):
            if arrays[i][0]<m:
                m=arrays[i][0]
                mm=i
        for j in range(len(arrays)):
            if j!=mm and n<arrays[j][len(arrays[j])-1]:
                n=arrays[j][len(arrays[j])-1]
                nn=j
        a=abs(n-m)
       # print(n,m)
        m,n=-999999999,9999999999
        mm,nn=-1,-1
        for i in range(len(arrays)):
            if arrays[i][len(arrays[i])-1]>m:
                m=arrays[i][len(arrays[i])-1]
                mm=i
       # print(mm)
        for j in range(len(arrays)):
            if j!=mm and n>arrays[j][0]:
                n=arrays[j][0]
                nn=j
       # print(n,m)
        b=abs(n-m)
        if a>b:
            return a
        return b
