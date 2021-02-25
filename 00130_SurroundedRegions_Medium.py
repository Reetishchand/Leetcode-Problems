'''Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
  Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:
Input: board = [["X"]]
Output: [["X"]]
  Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.'''
 
class Solution:
    def solve(self, arr: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(arr)==0:
            return
        bz=[]
        nbz=[]
        m,n = len(arr),len(arr[0])
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if arr[i][j]=="O":
                        bz.append([i,j])
                        continue
                if arr[i][j]=="O":
                    arr[i][j]="T"
        
        print(bz)
        while len(bz)>=1:
            cur = bz.pop()
            print(cur)
            x,y=cur[0],cur[1]
            if x+1<m and arr[x+1][y]=="T":
                arr[x+1][y]="O"
                bz.append([x+1,y])
            if y+1<n and arr[x][1+y]=="T":
                arr[x][y+1]="O"
                bz.append([x,y+1])
            if x-1>=0 and arr[x-1][y]=="T":
                arr[x-1][y]="O"
                bz.append([x-1,y])
            if y-1>=0 and arr[x][y-1]=="T":
                arr[x][y-1]="O"
                bz.append([x,y-1])
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if arr[i][j]=="T":
                    arr[i][j]="X"
            
        
        
        
