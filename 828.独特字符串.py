'''
@Description: 
@Author: k.chen
@Date: 2019-12-27 17:27:41
@LastEditTime : 2020-01-04 17:39:41
'''
#
# @lc app=leetcode.cn id=828 lang=python3
#
# [828] 独特字符串
#

# @lc code=start
class Solution:
    def uniqueLetterString(self, S: str) -> int:
        list_s = list(S)
        length = len(list_s)
        index = dict()
        ans = 0
        for (i,c) in enumerate(list_s):
            if c in index:
                index[c].append(i)
            else:
                index[c] = [-1,i]
        for key in index:
            index[key].append(length)
        for key in index:
            #print(key)
            temp_list = index[key]
            temp_ans = 0
            for (i,j) in enumerate(temp_list):
                if i== 0 or i == len(temp_list)-1:
                    continue
                ans += (temp_list[i]-temp_list[i-1])*(temp_list[i+1]-temp_list[i])%(10**9+7)
        return ans
# @lc code=end