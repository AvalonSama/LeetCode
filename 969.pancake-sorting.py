'''
@Description: 
@Author: k.chen
@Date: 2019-06-25 21:20:23
@LastEditTime: 2019-06-25 21:21:57
'''
#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#
import copy
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        temp_A = copy.deepcopy(A)
        temp_A.sort()
        temp_A.reverse()
        for (i,num) in enumerate(temp_A):
            index = A.index(num)
            result.append(index+1)
            result.append(len(A)-i)
            temp = A[0:index+1]
            temp.reverse()
            A[0:index+1]=temp
            temp = A[0:len(A)-i]
            temp.reverse()
            A[0:len(A)-i] = temp
        return result
