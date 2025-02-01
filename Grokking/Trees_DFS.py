class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def MinimumSumPath(self, node):
        if node is None:
            return float('inf')

        if node.left is None and node.right is None:
            return node.val

        leftSum = self.MinimumSumPath(node.left)
        rightSum  =self.MinimumSumPath(node.right)

        return node.val + min(leftSum, rightSum)

    def ValidateSumPath(self, node, sum):
        if node is None :
            return False

        if node.val == sum and node.left is None and node.right is None:
            return True

        return self.ValidateSumPath(node.left, sum - node.val) or self.ValidateSumPath(node.right, sum - node.val)

# Example usage
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(20)


solution = Solution()

print(solution.ValidateSumPath(root1,15)) # Output: 15


