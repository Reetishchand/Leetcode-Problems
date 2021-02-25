'''Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
  Example 1:
Input: "()"
Output: 1
Example 2:
Input: "(())"
Output: 2
Example 3:
Input: "()()"
Output: 2
Example 4:
Input: "(()(()))"
Output: 6
  Note:
S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50'''
 
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        S=S.replace("()","1").replace("(1)","2")
        st=[]
        s=0
        for i in range(len(S)):
            if S[i]!=")":
                st.append(S[i])
            else:
                curScore=0
                while st[-1]!="(":
                    curScore+=int(st.pop())
                st.pop()
                st.append(str(2*curScore))                
        print(st)
        while(len(st))!=1:
            x=st.pop()
            y=st.pop()
            st.append(str(int(x)+int(y)))
        return int(st[-1])
