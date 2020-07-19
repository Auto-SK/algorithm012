# 1. 递归解法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if (not root):
                return 0
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        ans = []
        dfs(root)
        return ans

# 2. 迭代解法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return ans