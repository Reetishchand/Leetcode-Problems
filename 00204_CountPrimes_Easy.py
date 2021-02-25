'''Count the number of prime numbers less than a non-negative number, n.
  Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:
Input: n = 0
Output: 0
Example 3:
Input: n = 1
Output: 0
  Constraints:
0 <= n <= 5 * 106'''
 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n>2:
            n-=1
            arr=[1]*(n+1)
            arr[0]=arr[1]=0
            p=2
            while p*p<=n:
                if arr[p]==1:
                    for i in range(p*p,n+1,p):
                        arr[i]=0
                p+=1
            return sum(arr)
        return 0
                
