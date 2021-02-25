'''Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
  Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
  Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter'''
 
class Solution:
    def gethash(self,s):
        hs={}
        for i in range(len(s)):
            try:
                hs[s[i]]+=1
            except:
                hs[s[i]]=1
        return hs
    
    def compareDic(self,d1,d2):
        for i in d1.keys():
            if i in d2 :
                d1[i]=min(d1[i],d2[i])
            else:
                d1[i]=-1
           
        return d1
        
    def commonChars(self, A: List[str]) -> List[str]:
        hs=self.gethash(A[0])
    #    print(hs)
        for i in range(1,len(A)):
            d = self.gethash(A[i])
        #    print(d)
            hs = self.compareDic(hs,d)
   #         print(hs)
        ans=[]
        for i in hs.keys():
            for j in range(hs[i]):
                ans.append(i)
        return ans
                    
