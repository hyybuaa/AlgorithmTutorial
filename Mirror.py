# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def mirror(self, root):
        # write code here
        if root != None:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.mirror(root.left)
            self.mirror(root.right)
        return root

if __name__ == "__main__":
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    solution = Solution()
    result = solution.mirror(pRoot)
    print(result)