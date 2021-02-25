'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
  Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
  Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.'''
 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs={}
        arr=[]
        if len(strs)<=1:
            return [strs]
        for i in range(len(strs)):
            arr.append(''.join(sorted(strs[i])))
        for i in range(len(arr)):
            try:
                hs[arr[i]].append(strs[i])
            except:
                hs[arr[i]]=[strs[i]]
                
        return hs.values()
        
