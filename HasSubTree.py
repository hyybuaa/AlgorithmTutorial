# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == pRoot2:
            return True
        if pRoot2 == None:
            return False
        if pRoot1 == None:
            return False
        result = False
        # 值一样的情况
        if pRoot1.val == pRoot2.val:
            result = self.match(pRoot1, pRoot2)
        if result:
            return True
        # 值不一样的情况
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def match(self, root1, root2):
        if root1 == root2:
            return True
        if root2 == None:
            return True
        if root1 == None:
            return False
        result = False
        if root1.val == root2.val:
            result = self.match(root1.left, root1.left) and self.match(root1.right, root2.right)
        return result

if __name__ == "__main__":
    pRoot1 = TreeNode(1)
    pRoot1.left = TreeNode(2)
    pRoot1.right = TreeNode(3)
    pRoot2 = TreeNode(3)
    solution = Solution()
    result = solution.HasSubtree(pRoot1, pRoot2)
    print(result)