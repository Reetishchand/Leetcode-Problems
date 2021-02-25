'''Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.
 '''
 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t={}
        arr=[]
        for i in nums1:
            t[i]=1
        for i in nums2:
            try:
                t[i]+=1
            except:
                pass
        for i in t.keys():
            if t[i]>=2:
                arr.append(i)
        return arr
