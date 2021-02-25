'''Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.'''
 
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        n1=a.split("+")
        n2=b.split("+")
        print(n1,n2)
        ans=[0,0]
        ans[0]=str((int(n1[0])*int(n2[0]))-(int(n1[1].replace("i",""))*int(n2[1].replace("i",""))))
        
        ans[1]=str((int(n1[1].replace("i",""))*int(n2[0])) + (int(n2[1].replace("i","")) * int(n1[0])))+"i"
        print(int(n1[1].replace("i",""))*int(n2[0]))
        print(int(n2[1].replace("i","")) * int(n2[0]))
        return '+'.join(ans)
        
                    
        
