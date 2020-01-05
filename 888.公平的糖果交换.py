'''
@Description: 
@Author: k.chen
@Date: 2020-01-04 17:43:23
@LastEditTime : 2020-01-05 21:32:38
'''
#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def binarySearch(self,A,x):
        l = 0
        r = len(A)-1
        mid = (r+l)//2
        while(l<r):
            if A[mid] < x:
                l = mid+1
            elif A[mid]>x:
                r = mid-1
            else:
                return True
            mid = (r+l)//2
        if A[l]!=x:
            return False
        else:
            return True
    def fairCandySwap(self, A, B) :
        A = sorted(A)
        B = sorted(B)
        sum_A = sum(A)
        sum_B = sum(B)
        for i in A:
            tA = sum_A - i
            tB = sum_B + i
            if (tB-tA) % 2 != 0:
                continue
            if self.binarySearch(B,(tB-tA)//2):
                return [i,(tB-tA)//2]
# @lc code=end

