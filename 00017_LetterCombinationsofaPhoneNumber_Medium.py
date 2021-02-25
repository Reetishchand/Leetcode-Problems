'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
  Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
Input: digits = ""
Output: []
Example 3:
Input: digits = "2"
Output: ["a","b","c"]
  Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].'''
 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return 
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if len(digits)==1:
            return phone[digits[0]]
        sofar=digits[0]
        def helper(k1,k2):
            l1=phone[k1]
            l2=phone[k2]
            lis=[]
            for i in range(len(l1)):
                for j in range(len(l2)):
                    lis.append(l1[i]+l2[j])
            # self.temp=self.ans[:]
            
            phone[k1+k2]=lis
        
        for i in range(1,len(digits)):
            helper(sofar,digits[i])
            sofar+=digits[i]
        return phone[digits]
      
            
