'''
@Description: 
@Author: k.chen
@Date: 2020-01-24 15:31:26
@LastEditTime : 2020-01-24 23:57:33
'''
#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#
# https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/
#
# algorithms
# Easy (58.67%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 7.2K
# Testcase Example:  '["cbd"]\n["zaaaz"]'
#
# 我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
# 
# 例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
# 
# 现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足
# f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。
# 
# 
# 
# 示例 1：
# 
# 输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
# 
# 
# 示例 2：
# 
# 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] 都是小写英文字母
# 
# 
#

# @lc code=start
class Solution:
    
    def f(self, word):
        from collections import Counter
        temp = sorted(Counter(word).items(), key= lambda item: item[0])
        return temp[0][1]
    # def binarySearch(self, num_list, target):
    #     l = 0
    #     r = len(num_list) - 1
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        num_queries = []
        num_words = []
        for word in queries:
            num_queries.append(self.f(word))
        for word in words:
            num_words.append(self.f(word))
        num_words = sorted(num_words, reverse=True)
        ans = []
        # print(num_queries)
        # print(num_words)
        for num in num_queries:
            temp_ans = 0
            for count in num_words:
                # print(count)
                if num < count:
                    temp_ans += 1
                else:
                    break
            ans.append(temp_ans)
        return ans    
# @lc code=end

