# 1. 递归解法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if (not root):
                return 0
            ans.append(root.val)
            for child in root.children:
                dfs(child)
        ans = []
        dfs(root)
        return ans

# 2. 迭代解法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = bool(root) * [root]
        ans = []
        while (stack):
            root = stack.pop()
            ans.append(root.val)
            stack += root.children[::-1]
        return ans
