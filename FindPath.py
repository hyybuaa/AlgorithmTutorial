from copy import deepcopy

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def findPath(self, root, exceptNumber):
        if root == None:
            return None
        result = []
        path = []
        result = self.dfs(root, result, path, exceptNumber)
        return result

    def dfs(self, root, result, path, exceptNumber):
        # 没有下一个子节点
        path.append(root.val)
        if root.left == None and root.right == None and sum(path) == exceptNumber:
            result.append(deepcopy(path))
        if root.left != None:
            self.dfs(root.left, result, path, exceptNumber)
        if root.right != None:
            self.dfs(root.right, result, path, exceptNumber)
        path.pop()
        return result

if __name__ == "__main__":
    pRoot = TreeNode(1)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(3)
    exceptNumber = 4
    solution = Solution()
    result = solution.findPath(pRoot, exceptNumber)
    print(result)