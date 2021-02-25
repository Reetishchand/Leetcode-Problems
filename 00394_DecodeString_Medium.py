'''Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
  Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
  Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].'''
 
class Solution:
    def decodeString(self, s: str) -> str:
        ans=""
        val=[]
        num=[]
        for i in range(len(s)):
        #    print("s[i] :",s[i])
            if s[i].isnumeric():
                if i-1>=0 and s[i-1].isnumeric():
                    x=num.pop()
                    x=str(x)+s[i]
                    num.append(int(x))
                else:
                    num.append(int(s[i]))
            elif s[i]=="]":
                temp=""
                r=num.pop()
                while val and val[-1]!='[':
                    temp = val.pop()+temp
                print(val)
                if val[-1]=='[':
                    val.pop()
                if val and val[-1]!='[':
                    val[-1]=val[-1]+(temp*r)
                else:
                    val.append(temp*r)
                
            else:
                val.append(s[i])
        
        
      
        while val:
            if val[-1]=='[':
                val.pop()
            else:
                if num:
                    r=num.pop()
                else:
                    r=1
                ans=(val.pop()*r)+ans
                #print("vl:",val.pop())
        return ans
            
