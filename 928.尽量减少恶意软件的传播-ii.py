'''
@Description: 
@Author: k.chen
@Date: 2020-01-25 22:46:39
@LastEditTime : 2020-01-30 22:15:39
'''
#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#
# https://leetcode-cn.com/problems/minimize-malware-spread-ii/description/
#
# algorithms
# Hard (38.08%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    582
# Total Submissions: 1.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]\n[0,1]'
#
# (这个问题与 尽量减少恶意软件的传播 是一样的，不同之处用粗体表示。)
# 
# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。
# 
# 一些节点 initial
# 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
# 
# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
# 
# 我们可以从初始列表中删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。如果移除这一节点将最小化 M(initial)，
# 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输出：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输入：0
# 
# 
# 示例 2：
# 
# 输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 < graph.length = graph[0].length <= 300
# 0 <= graph[i][j] == graph[j][i] <= 1
# graph[i][i] = 1
# 1 <= initial.length < graph.length
# 0 <= initial[i] < graph.length
# 
# 
#

# @lc code=start
class Solution:
    def minMalwareSpread(self, graph, initial):
        from queue import Queue
        q = Queue()
        point_num = len(graph)
        count_list = [[] for i in range(point_num)] 
        for i in initial:
            flag = [0] * point_num
            while not q.empty():
                q.get()
            q.put(i)
            count_list[i].append(i)
            while not q.empty():
                now_point = q.get()
                for (j,v) in enumerate(graph[now_point]):
                    if v == 1 and flag[j] == 0 and j not in initial:
                        q.put(j)
                        flag[j] = 1
                        #print(count_list)
                        count_list[j].append(i)
        ans_list = [0] * point_num
        for i in count_list:
            if len(i) == 1:
                ans_list[i[0]] += 1
        #print(ans_list)
        ans = 0
        max_num = -1
        for i,j in enumerate(ans_list):
            #print(max_num)
            if j>max_num:
                max_num = j
                ans = i
        return ans  
# s = Solution()
# print(s.minMalwareSpread([[1,1,0],[1,1,1],[0,1,1]],[0,1]))
# @lc code=end