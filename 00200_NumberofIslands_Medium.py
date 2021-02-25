'''Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
  Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
  Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.'''
 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        hs={}
        ic=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    hs[str(i)+' '+str(j)]=0
        print(hs)
        for i in hs.keys():
            #print(i)
            if hs[i]==0:
                x,y=map(int,i.split(" "))
                ic+=1
                arr=[[x,y]]
                
                while len(arr):
                    som = arr.pop()
                    r,c = som[0],som[1]
                    serach1 = str(r)+' '+str(c)
                    hs[serach1]=1
                    
                    if r-1>=0 and grid[r-1][c]=="1":
                        serach = str(r-1)+' '+str(c)
                        if hs[serach]==0:
                            arr.append([r-1,c])
                    if c-1>=0 and grid[r][c-1]=="1":
                        serach = str(r)+' '+str(c-1)
                        if hs[serach]==0:
                            arr.append([r,c-1])
                    if c+1<len(grid[r]) and grid[r][c+1]=="1":
                        serach = str(r)+' '+str(c+1)
                        if hs[serach]==0:
                            arr.append([r,c+1])
                    if r+1<len(grid) and grid[r+1][c]=="1":
                        serach = str(r+1)+' '+str(c)
                        if hs[serach]==0:
                            arr.append([r+1,c])
        
        return ic
                
                
                
                
                
            
        
