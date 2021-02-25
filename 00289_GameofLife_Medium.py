'''According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
  Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
  Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
  Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?'''
 
class Solution:
    
    def findLive(self,board,i,j):
        m,n=len(board),len(board[0])
        live=0
        if 1+i<m and board[i+1][j]==1:
            live+=1
        if i+1<m and 1+j<n and board[i+1][j+1]==1:
            live+=1 
        if i>0 and board[i-1][j]==1:
            live+=1
        if i>0 and j>0 and board[i-1][j-1]==1:
            live+=1 
        
        if 1+j<n and board[i][1+j]==1:
            live+=1
        if i+1<m and j>0 and board[i+1][j-1]==1:
            live+=1 
        if j>0 and board[i][j-1]==1:
            live+=1
        if i>0 and j+1<n and board[i-1][j+1]==1:
            live+=1
        return live
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        changes=[]
        for i in range(m):
            for j in range(n):
                # print(str(i)+" "+str(j)+" "+str(self.findLive(board,i,j)))
                if board[i][j]==0:
                    if self.findLive(board,i,j)==3:
                        changes.append([i,j])
                elif board[i][j]==1:
                    cur = self.findLive(board,i,j)
                    if cur<2 or cur>3:
                        changes.append([i,j])
        print(changes)
        for i in range(len(changes)):
            x,y=changes[i][0],changes[i][1]
            # print(board[i])
            if board[x][y]==0:
                board[x][y]=1
            else:
                board[x][y]=0
        
                    
        
