'''On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
  Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
  Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.'''
 
class Solution:
    def isRobotBounded(self, s: str) -> bool:
        dr=["N","W","S","E"]
        cur=0
        #l +1 #r -1
        pos=[0,0]
        circle=False
        c=0
        upperLimit=0
        while circle==False:
            now = s[c]
            if now=="G":
                d=dr[cur]
                if d=="N":
                    pos[1]+=1
                elif d=="S":
                    pos[1]-=1
                elif d=="E":
                    pos[0]+=1
                else:
                    pos[0]-=1
                
                #print(pos)
            elif now=="L":
                cur+=1
            elif now=="R":
                cur-=1
            
            if cur>3:
                cur=0
            elif cur<0:
                cur=3
            c+=1
            if c>=len(s):
                c=0
                if now=="N":
                    return False
                if pos ==[0,0]:
                    circle=True
                upperLimit+=1
                if upperLimit==5:
                    return False
        return circle
            
                
                
                    
                
            
