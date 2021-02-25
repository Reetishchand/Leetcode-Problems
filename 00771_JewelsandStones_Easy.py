'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
  Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
  Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.'''
 
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(J)==0:
            return 0
        count=0
        myhash={}
        for i in J:
            myhash[i]=1
        for i in S:
            try:
                x=myhash[i]
                count+=1
            except:
                #print()
                x=0
        return count
                
