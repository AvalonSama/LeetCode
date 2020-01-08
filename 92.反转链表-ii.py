'''
@Description: 
@Author: k.chen
@Date: 2020-01-05 22:12:05
@LastEditTime : 2020-01-08 22:19:20
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, start, end, num):
        pre_node = None
        now_node = start
        count = 0

        while count < num:
            count+=1
            next_node = now_node.next
            now_node.next = pre_node
            pre_node = now_node
            now_node = next_node
        return start, end

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n==m:
            return head
        count = 1
        now_node = head
        pre_node = None
        start_node = now_node
        temp_pre_node = None
        while count<n:
            if count == m:
                pre_node = temp_pre_node
                start_node = now_node
            count += 1
            temp_pre_node = now_node
            now_node = now_node.next
        end_node = now_node
        post_node = end_node.next
        print(start_node, end_node)
        #print(pre_node)
        start_node, end_node = self.reverse(start_node, end_node, n-m+1)
        start_node.next = post_node
        if pre_node != None:
            pre_node.next = end_node
        else:
            head = end_node
        return head


# @lc code=end

