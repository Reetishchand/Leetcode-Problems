'''Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.'''
 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        if len(s)==0 or s==s[::-1]:
            return True
        i,j=0,len(s)-1
        once = False
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                s1 = s[:i]+s[i+1:]
                s2 = s[:j]+s[j+1:]
                return s1==s1[::-1] or s2 == s2[::-1]
        return True
            
            
