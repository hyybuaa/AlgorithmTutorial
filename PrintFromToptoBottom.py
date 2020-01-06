# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root != None:
            lst = []
            lst2 = []
            lst.append(root)
            while(lst != []):
                curTree = lst.pop(0)
                lst2.append(curTree.val)
                if curTree.left != None:
                    lst.append(curTree.left)
                if curTree.right != None:
                    lst.append(curTree.right)
        else:
            lst2 = []
        return lst2

if __name__ == "__main__":
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    solution = Solution()
    result = solution.PrintFromTopToBottom(pRoot)
    print(result)