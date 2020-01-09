class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PreSearch(root):
    result = dfs(root, [])
    return result

def dfs(root, result):
    if root != None:
        result.append(root.val)
    if root.left != None:
        result = dfs(root.left, result)
    if root.right != None:
        result = dfs(root.right, result)
    return result

if __name__ == "__main__":
    pRoot1 = TreeNode(1)
    pRoot1.left = TreeNode(2)
    pRoot1.right = TreeNode(3)
    pRoot2 = TreeNode(5)
    pRoot2.left = pRoot1
    pRoot2.right = pRoot1
    result = PreSearch(pRoot2)
    print(result)
   




    