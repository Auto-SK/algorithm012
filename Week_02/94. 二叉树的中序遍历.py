# 1. 递归解法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        ans = []
        dfs(root)
        return ans

# 2. 迭代解法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans