'''Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
  Example 1:
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:
Input: s = "aeiou"
Output: ""
  Constraints:
1 <= s.length <= 1000
s consists of only lowercase English letters.'''
 
class Solution:
    def removeVowels(self, s: str) -> str:
        s1=""
        for i in range(len(s)):
            if s[i] in "aeiou" or s[i] in "AEIOU":
                continue
            s1+=s[i]
        return s1
