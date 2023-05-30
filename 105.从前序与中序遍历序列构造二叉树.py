# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """


# test case 1
# preorder: [3, 9, 20, 15, 7]
# inorder: [9, 3, 15, 20, 7]


# 规律总结
# preorder: [3, 9, 20, 15, 7]
# parent -> left -> right


# inorder: [9, 3, 15, 20, 7]
# left -> parent -> right
# 有 left 先 print left，然后在看 right 是否为 parent

# postorder: [9, 15, 7, 20, 3]
# left -> right -> parent
# 最后一个是 parent node




# test case 2
# preorder: [-1]
# inorder: [-1]
# ouput: [-1]

