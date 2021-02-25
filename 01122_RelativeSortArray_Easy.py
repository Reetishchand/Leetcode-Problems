'''Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
  Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
  Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.'''
 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        myhash={}
        k=0
        for i in arr1:
            try:
                myhash[i]+=1
            except:
                myhash[i]=1
        for i in range(len(arr2)):
            rep = myhash[arr2[i]]
            for j in range(rep):
                arr1[k]=arr2[i]
                k+=1
            myhash.pop(arr2[i])
        for i in sorted(myhash.keys()):
            rep = myhash[i]
            for j in range(rep):
                arr1[k]=i
                k+=1
        return arr1
        
            
        
