'''You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
  Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
  Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.'''
 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q=[]
        c=0
        fresh=0
        time=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return time
        
        while q:
            time+=1
            temp=[]
            for i in range(len(q)):
                i,j=q[-1][0],q[-1][1]
                q.pop()
                if i+1<len(grid) and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    temp.append([i+1,j])
                    fresh-=1
                if j+1<len(grid[i]) and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    temp.append([i,j+1])
                    fresh-=1
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    temp.append([i-1,j])
                    fresh-=1
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    temp.append([i,j-1])
                    fresh-=1
            q=temp[:]
            if fresh==0:
                return time
        if fresh==0:
                return time
        return -1
        
            

