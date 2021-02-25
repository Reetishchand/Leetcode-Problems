'''A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
  Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
  Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
 '''
 
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S)==0:
            return []
        dic={}
        for i in range(len(S)):
            try:
                dic[S[i]][1]=i
            except:
                dic[S[i]]=[i,i]
    #    print(dic)
        
        st=[]
        for i in dic.keys():
            if len(st)==0:
                st.append(dic[i])
            else:
                cur=dic[i]
                if cur[0]>st[-1][1]:
                    st.append(cur)
                elif cur[0]<st[-1][1] and cur[1]>st[-1][1]:
                    st[-1][1]=cur[1]
        
        ans=[]
        for i in range(len(st)):
            ans.append(st[i][1]+1-st[i][0])
        return ans
        
