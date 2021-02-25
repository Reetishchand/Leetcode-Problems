'''Convert a non-negative integer num to its English words representation.
  Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
  Constraints:
0 <= num <= 231 - 1'''
 
class Solution:

    dic={}
    tens={}
    def words(self,n,c):
        ans=[]
        while n>0:
            x=n%10
            if len(ans)==0:
                ans.append(self.dic[x][0])
            elif len(ans)==1:
                ans.append(self.dic[x][1])
                if len(ans)==2 and ans[-1]+" "+ans[-2] in self.tens:
                    x1=ans[-1]
                    ans.pop()
                    x2=ans[-1]
                    ans.pop()
                    ans.append(self.tens[x1+" "+x2])
                    ans.append("Zero")
            elif len(ans)==2:
                ans.append("Hundred")
                ans.append(self.dic[x][0])
            n=n//10
        ans=ans[::-1]
        if ans and c==2:
            ans.append("Thousand")
        elif ans and c==3:
            ans.append("Million")
        elif ans and c==4:
            ans.append("Billion")
        return ans
        
                
    
    
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        self.dic[1]=["One","Ten"]
        self.dic[2]=["Two","Twenty"]
        self.dic[3]=["Three","Thirty"]
        self.dic[4]=["Four","Forty"]
        self.dic[5]=["Five","Fifty"]
        self.dic[6]=["Six","Sixty"]
        self.dic[7]=["Seven","Seventy"]
        self.dic[8]=["Eight","Eighty"]
        self.dic[9]=["Nine","Ninety"]
        self.dic[0]=["Zero","Zero"]
        self.tens["Ten One"]="Eleven"
        self.tens["Ten Two"]="Twelve"
        self.tens["Ten Three"]="Thirteen"
        self.tens["Ten Four"]="Fourteen"
        self.tens["Ten Five"]="Fifteen"
        self.tens["Ten Six"]="Sixteen"
        self.tens["Ten Seven"]="Seventeen"
        self.tens["Ten Eight"]="Eighteen"
        self.tens["Ten Nine"]="Nineteen"
        
        
        temp=num
        ans=[]
        c=0
        while temp>0:
            x = temp%1000
            c+=1
            if str(x)!="000":
                ans=self.words(x,c)+ans
            temp=temp//1000
        s=""
        for i in range(len(ans)):
            if ans[i]!="Zero":
                s+=ans[i]+" "
        return s.strip()
            
            
            
        
