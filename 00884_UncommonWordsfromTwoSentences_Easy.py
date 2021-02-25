'''We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.
  Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
  Note:
0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.'''
 
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        myhash={}
        for i in A.split(" "):
            try:
                myhash[i]+=1
            except:
                myhash[i]=1
        for i in B.split(" "):
            try:
                myhash[i]+=1
            except:
                myhash[i]=1
        ans=[]
        for i in myhash.keys():
            if myhash[i]==1:
                ans.append(i)
        return ans
                
        
