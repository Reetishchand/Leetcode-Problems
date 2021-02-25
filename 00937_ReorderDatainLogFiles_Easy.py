'''You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
  Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
  Constraints:
1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.'''
 
class Solution:
    
    def sortLet(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            L,R=arr[:mid],arr[mid:]
            self.sortLet(L)
            self.sortLet(R)
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if (L[i][1]<R[j][1]) or (L[i][1]==R[j][1] and L[i][0]<R[j][0]):
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
            
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs)==1:
            return logs
        res=[]
        alp=[]
        dig=[]
        for i in range(len(logs)):
            t=logs[i].split(" ")
            if t[1].isdigit():
                dig.append([t[0],' '.join(t[1:])])
            else:
                alp.append([t[0],' '.join(t[1:])]) 
       
                 
        self.sortLet(alp)
        for i in range(len(alp)):
            alp[i] = alp[i][0]+' '+alp[i][1]
            
        for i in range(len(dig)):
            t = dig[i][0]+' '+dig[i][1]
            alp.append(t)
        return alp
        
