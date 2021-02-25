'''Given a string, determine if a permutation of the string could form a palindrome.
Example 1:
Input: "code"
Output: false
Example 2:
Input: "aab"
Output: true
Example 3:
Input: "carerac"
Output: true'''
 
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic={}
        for i in range(len(s)):
            try:
                dic[s[i]]+=1
            except:
                dic[s[i]]=1
        odd=0
        print(dic)
        for i in dic.keys():
            if dic[i]%2!=0:
                odd+=1
        if odd>1:
            return False
        return True
        
