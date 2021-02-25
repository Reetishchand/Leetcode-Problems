'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
  Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
  Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length'''
 
class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        if n==0:
            return True
        if len(arr)==1:
            if arr[0]==0 and n==1:
                return True
            else:
                return False
        if len(arr)==2 and sum(arr)==0 and n==1:
            return True        
        if len(arr)>2:
            for i in range(len(arr)):
                if (i==0 and arr[i]==0 and arr[i+1]==0):
                    arr[i]=1
                    n-=1
                elif (i==(len(arr)-1) and arr[i]==0 and arr[i-1]==0):
                    arr[i]=1
                    n-=1
                else:
                    if (arr[i]==0 and arr[i-1]==0 and arr[i+1]==0):
                        arr[i]=1
                        n-=1
                if n==0:
                    return True
        return n==0
        
