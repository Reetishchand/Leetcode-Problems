'''Given an integer n, return any array containing n unique integers such that they add up to 0.
  Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:
Input: n = 3
Output: [-1,0,1]
Example 3:
Input: n = 1
Output: [0]
  Constraints:
1 <= n <= 1000'''
 
class Solution:
    def sumZero(self, n: int) -> List[int]:
        c=0
        ans=[]
        if n%2==0:
            c=n
        else:
            c=n-1
        
        for i in range(c,0,-2):
            ans.append(i)
            ans.append(i*-1)
        if n%2!=0:
            ans.append(0)
        return ans
