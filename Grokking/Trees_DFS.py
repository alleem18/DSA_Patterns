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



    def findPaths(self, root, required_sum):
        allPaths = []
        self.findPaths_recursive(root, required_sum, [], allPaths)
        return allPaths

    def findPaths_recursive(self, currentNode, required_sum, currentPath, allPaths):
        if currentNode is None:
            return

        # add the current node to the path
        currentPath.append(currentNode.val)

        # if the current node is a leaf and its value is equal to required_sum, save the
        # current path
        if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
        else:
            # traverse the left sub-tree
            self.findPaths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
            # traverse the right sub-tree
            self.findPaths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del currentPath[-1]


    def sumOfPathNumbers(self, root):
        return self.recursiveFunctionForsumOfPathNumbers(root, 0)


    def recursiveFunctionForsumOfPathNumbers(self, currnode, pathsum):
        if currnode is None:
            return 0
        pathsum = pathsum * 10 + currnode.val
        if currnode and currnode.left is None and currnode.right is None:
            return pathsum

        return  self.recursiveFunctionForsumOfPathNumbers(currnode.left, pathsum) + self.recursiveFunctionForsumOfPathNumbers(currnode.right, pathsum)



# Example usage
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
required_sum = 23
sol = Solution()
print( str(sol.sumOfPathNumbers(root)))





