'''Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
  Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
  Constraints:
1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.'''
 
class Solution:
    def compress(self,name):
        arr=[]
        for i in range(len(name)):
            if arr and arr[-1][0]==name[i]:
                arr[-1][1]+=1
            else:
                arr.append([name[i],1])
        return arr
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name==typed:
            return True
        if len(name)>len(typed):
            return False
        arr=self.compress(name)
        typ = self.compress(typed)
       # print(arr,typ)
        if len(arr)!=len(typ):
            return False
        for i in range(len(typ)):
            if typ[i][0]!=arr[i][0] or typ[i][1]<arr[i][1]:
                return False
        return True
        
                
            
