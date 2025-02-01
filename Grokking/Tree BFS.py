
from collections import deque
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
    def connect(root):
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

    ''' 
        Input: root = [1, 2, 3, 4, 5, 6, 7]
        Expected
        Output: [1, 3, 7]
        Justification: The last node at level 0 is 1.
        The last node at level1 is 3.
        The last node at level2 is 7.
        
    '''
    def rightViewofBinaryTree(self, root):
        result = []
        if not root :
            return root
        queue = deque()
        queue.append(root)

        while queue:
            currlevel = len(queue)
            for _ in range(currlevel):
                currnode = queue.popleft()
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)

            result.append(currnode.val)
        return result

'''sol = Solution()
newNode = sol.rightViewofBinaryTree(node)
print(newNode)
'''

node = TreeNode(12)
node.left = TreeNode(7)
node.left.right = TreeNode(9)
node.left.right.right = TreeNode(3)
node.right = TreeNode(1)
node.right.left = TreeNode(10)
node.right.right = TreeNode(5)


def printnode(newNode):
    res = []
    queue = deque()
    queue.append(node)
    while queue:
        currlevel = len(queue)
        for _ in range(currlevel):
            currnode = queue.popleft()
            res.append(currnode.val)
            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)
    return res




