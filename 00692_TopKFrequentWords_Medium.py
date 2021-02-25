'''Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ? k ? number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.'''
 
class Solution:
    
    def sort(self,lis):
        if len(lis)>1:
            mid=len(lis)//2
            L,R=lis[:mid],lis[mid:]
            self.sort(L)
            self.sort(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if (L[i][1]>R[j][1]) or (L[i][1]==R[j][1] and L[i][0]<R[j][0]) :
                    lis[k]=L[i]
                    i+=1
                else :
                    lis[k]=R[j]
                    j+=1
                k+=1
            
            while i<len(L):
                lis[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                lis[k]=R[j]
                j+=1
                k+=1
        return lis
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        ans=[]
        lis=[]
        for i in range(len(words)):
            try:
                dic[words[i]]+=1
            except:
                dic[words[i]]=1
        
        for i in dic.keys():
            lis.append([i,dic[i]])
        self.sort(lis)
        for i in range(k):
            ans.append(lis[i][0])
        return ans
