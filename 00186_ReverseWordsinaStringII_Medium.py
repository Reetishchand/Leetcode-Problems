'''Given an input string , reverse the string word by word. 
Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?'''
 
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        print(s)
        
        i=0
        last=-1
        s.append(" ")
        while i<len(s):
            if s[i]==" ":
                x,y=last+1,i-1
                while x<y:
                    s[x],s[y]=s[y],s[x]
                    x+=1
                    y-=1
                last=i
            i+=1
        s.pop()
        return s
            
