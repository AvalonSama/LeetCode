/*
 * @lc app=leetcode.cn id=951 lang=cpp
 *
 * [951] 分割数组
 *
 * https://leetcode-cn.com/problems/flip-equivalent-binary-trees/description/
 *
 * algorithms
 * Medium (48.40%)
 * Total Accepted:    443
 * Total Submissions: 912
 * Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
 *
 * 我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。
 * 
 * 只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。
 * 
 * 编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
 * [1,3,2,null,6,4,5,null,null,null,null,8,7]
 * 输出：true
 * 解释：We flipped at nodes with values 1, 3, and 5.
 * 
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 每棵树最多有 100 个节点。
 * 每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数。
 * 
 * 
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if(root1==NULL&&root2==NULL) return true;
        else if(root1==NULL||root2==NULL) return false;
        if(root1->val==root2->val)
        {
            TreeNode* root1left = root1->left;
            TreeNode* root1right = root1->right;
            TreeNode* root2left = root2->left;
            TreeNode* root2right = root2->right;
            return (flipEquiv(root1left,root2left)&&flipEquiv(root1right,root2right))||(flipEquiv(root1right,root2left)&&flipEquiv(root1left,root2right));
        }
        else 
        {
            return false;
        }
    }
};
