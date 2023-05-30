
import collections
import pdb


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        # Base case
        if not inorder:
            return None

        # The last element of postorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the position of the root in the inorder list
        root_index = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root
    

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

solu = Solution()
root = solu.buildTree(inorder, postorder)

def get_val(node):
    
    if root:
        node_queue.append(root)
    
    while node_queue:

        for i in range(len(node_queue)):
            current_node = node_queue.popleft()
    
            if current_node:
                result.append(current_node.val)
            
            if current_node.left:
                node_queue.append(current_node.left)


            if current_node.right:
                node_queue.append(current_node.right)
                
node_queue = collections.deque()
result = []
get_val(root)
print(result)