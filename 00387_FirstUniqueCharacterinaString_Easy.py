'''Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
  Note: You may assume the string contains only lowercase English letters.'''
 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        hash={}
        for i in range(len(s)):
            try:
                hash[s[i]][1]+=1
            except:
                hash[s[i]]=[i,1]
      #  print(hash)
        min_ind=9999999999
        for i in hash.keys():
            if hash[i][1]==1:
                min_ind = min(min_ind,hash[i][0])
        
        return -1 if min_ind==9999999999 else min_ind
