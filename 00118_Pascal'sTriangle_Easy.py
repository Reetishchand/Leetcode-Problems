'''Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
  Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]
  Constraints:
1 <= numRows <= 30'''
 
class Solution:
    def generate(self, m: int) -> List[List[int]]:
        if m==0:
            return
        ans=[]
        if m==1:
            return [[1]]
        ans=[[1],[1,1]]
        for i in range(3,m+1):
            top = ans[-1]
            cur=[1]
            for j in range(len(top)-1):
                cur.append(top[j]+top[j+1])
            cur.append(1)
            ans.append(cur)
        return ans
