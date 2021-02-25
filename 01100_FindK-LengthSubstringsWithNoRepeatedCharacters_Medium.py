'''Given a string S, return the number of substrings of length K with no repeated characters.
  Example 1:
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:
Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.
  Note:
1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4'''
 
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        c=0
        for i in range(len(s)-k+1):
            if len(s[i:i+k]) == len(set(s[i:i+k])):
                c+=1
        return c
        
