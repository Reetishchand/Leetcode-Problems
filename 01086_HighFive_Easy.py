'''Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
  Example 1:
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
Example 2:
Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]
  Constraints:
1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.'''
 
class Solution:
    def merge(self,nums):
        if len(nums)>1:
            mid = len(nums)//2
            L,R = nums[:mid],nums[mid:]
            self.merge(L)
            self.merge(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]>R[j]:
                    nums[k]=L[i]
                    i+=1
                else:
                    nums[k]=R[j]
                    j+=1
                k+=1
            while i<len(L):
                nums[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                nums[k]=R[j]
                j+=1
                k+=1
        return nums
        
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans=[]
        myhash={}
        for i in range(len(items)):
            try:
                myhash[items[i][0]].append(items[i][1])
            except:
                myhash[items[i][0]]=[items[i][1]]
        for i in myhash.keys():
            if len(myhash[i])<=5:
                ans.append([i,sum(myhash[i])//5])
            else:
                lis = self.merge(myhash[i])
                ans.append([i,sum(lis[:5])//5])
        return ans
        
