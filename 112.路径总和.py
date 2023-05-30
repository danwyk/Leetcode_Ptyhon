import collections
import pdb


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
            
        def helper(node, current_sum):
            if node:
                current_sum += node.val
            
                helper(node.left, current_sum)
                helper(node.right, current_sum)
            
            if not node:
                sum_list.append(current_sum)
                current_sum = 0
            
        sum_list = []
        helper(root, 0)
        
        if targetSum in sum_list:
            return True
        
        return False

solu = Solution()
root = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node2 = TreeNode(2)
node7 = TreeNode(7)

root.left = node4
root.right = node8
node4.left = node11
node11.left = node7
node11.right = node2

print(solu.hasPathSum(root, 22))