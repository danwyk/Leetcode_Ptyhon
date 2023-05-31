# Definition for a binary tree node.
from typing import *
import collections
import pdb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        node_queue = collections.deque()
        
        if root != None:
            node_queue.append(root)
                
        while(node_queue):
            current_level = []
            size = len(node_queue)

            for i in range(size):
                current_node = node_queue.popleft()
                # pdb.set_trace()

                if current_node:
                    current_level.append(current_node.val)

                # if current_node.left != None:
                    node_queue.append(current_node.left)
                
                # if current_node.right != None:
                    node_queue.append(current_node.right)
            
            if current_level:
                result.append(current_level)
        
        return result


solu = Solution()
# input = [3, 9, 20, None, None, 15, 7]

root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

root.left = node9
root.right = node20
node20.left = node15
node20.right = node7

print(solu.levelOrder(root))