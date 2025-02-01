from queue import Queue

class TreeNode:
     def __init__(self, val = 0, left = None, right = None, next = None):
         self.val  = val
         self.right = right
         self.left = left
         self.next = next


class Solution:
    def sumofNodes(root):
        if not root:
            return root
        queue = Queue()
        queue.put(root)
        sum = 0
        while not queue.empty():

            currNode = queue.get()

            sum+= currNode.val

            if currNode.left:
                queue.put(currNode.left)

            if currNode.right:
                queue.put(currNode.left)
        return sum

from collections import deque

from queue import Queue

# class TreeNode:
#   def __init__(self, val):
#     self.val = val
#     self.left, self.right, self.next = None, None, None

# level order traversal using 'next' pointer
def print_level_order(root):
    curr = root
    res = []
    queue = deque([root])
    while queue:
        currlevel = len(queue)
        for _ in range(currlevel):
            currnode = queue.popleft()
            res.append(currnode.val)
            if currnode.next:
                res.append("#")
            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)

    return res

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(print_level_order(root))
class Solution:
    def connect(self, root):
        if root is None:
            return

        queue = Queue()
        queue.put(root)
        while not queue.empty():
            previousNode = None
            levelSize = queue.qsize()
            # connect all nodes of this level
            for _ in range(levelSize):
                currentNode = queue.get()
                if previousNode:
              
                    previousNode.next = currentNode
                previousNode = currentNode

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.put(currentNode.left)
                if currentNode.right:
                    queue.put(currentNode.right)
        return root


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root = sol.connect(root)

    print("Level order traversal using 'next' pointer: ")
    print(print_level_order(root))


main()

