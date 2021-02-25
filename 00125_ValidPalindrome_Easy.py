'''Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
  Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
  Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''
 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if i>len(s) or j<0:
                break
            # print(s[i],s[j])
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
            
        return True
