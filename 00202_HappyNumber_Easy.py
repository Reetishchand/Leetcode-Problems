'''Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
  Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:
Input: n = 2
Output: false
  Constraints:
1 <= n <= 231 - 1'''
 
class Solution:
    def findSq(self,n):
        ans=0
        while n>0:
            a=n%10
            ans+=(a**2)
            n=n//10
        return ans
    def isHappy(self, n: int) -> bool:
        visit=set([])
        while n!=1:
            n1 = self.findSq(n)
            if n1 in visit:
                return False
            visit.add(n1)
            n=n1
            print(n1)
        return True
        
