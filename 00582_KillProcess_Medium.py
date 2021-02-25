'''You have n processes. You are given two integer arrays pid and ppid, where the ID of the ith process is pid[i] and the ID of the parent process of the ith process is ppid[i].
Each process only has one parent process but may have one or more children processes. This is just like a tree structure. Only one process has ppid[i] that is 0, which means this process has no parent process.
Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.
  Example 1:
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Example 2:
Input: pid = [1], ppid = [0], kill = 1
Output: [1]
  Constraints:
n == pid.length
n == ppid.length
1 <= n <= 5 * 104
1 <= pid[i] <= 5 * 104
0 <= ppid[i] <= 5 * 104
Only one process has no parent.
All the values of pid are unique.
kill is guaranteed to be one of the values of pid.'''
 
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        hs={}
        for i in range(len(ppid)):
            try:
                hs[ppid[i]].append(pid[i])
            except:
                hs[ppid[i]]=[pid[i]]
        print(hs)
        ans=set([])
        q=[kill]
        counter=0
        while counter<len(q):
            cur=q[counter]
            counter+=1
            ans.add(cur)
            if cur in hs:
                for i in hs[cur]:
                    if i not in ans:
                        q.append(i)
        return list(ans)

            
            
        
