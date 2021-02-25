'''Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
  Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
  Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.'''
 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)==0:
            return
        k=2
        st=[]
        for i in range(len(s)):
            if st and st[-1][0]==s[i]:
                st[-1][1]+=1
            else:
                st.append([s[i],1])
            if st[-1][1]>=k:
                st.pop()
       # print(st)
        ans=""
        for i in st:
            ans+=i[0]*i[1]
        return ans
        
