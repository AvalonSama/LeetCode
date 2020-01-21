'''
@Description: 
@Author: k.chen
@Date: 2020-01-09 14:54:14
@LastEditTime : 2020-01-21 23:49:06
'''
#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (52.39%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 12.5K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
# 
# (注：分数越高的选手，排名越靠前。)
# 
# 示例 1:
# 
# 
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 
# 提示:
# 
# 
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
# 
# 
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        temp_nums = []
        for (i, j) in enumerate(nums):
            temp_nums.append([i,j])
        temp_nums = sorted(temp_nums, key = lambda x: -x[1])
        for (i,j) in enumerate(temp_nums):
            if i == 0:
                j.append("Gold Medal")
            elif i == 1:
                j.append("Silver Medal")
            elif i == 2:
                j.append("Bronze Medal")
            else:
                j.append(str(i+1))
        temp_nums = sorted(temp_nums, key = lambda x: x[0])
        ans = [i[2] for i in temp_nums]
        return ans
        
# @lc code=end

