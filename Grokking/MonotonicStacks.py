### Remove nodes from linkedlist

class Node:
    def __init__(self, val, next = None):
        self.next = next
        self.val = val


node1 = Node(5)
node2 = node1.next = Node(3)
node3 = node2.next = Node(7)
node4 = node3.next= Node(4)
node5 = node4.next = Node(2)
node5.next = Node(1)
node5.next.next = None

curr = node1
while curr:
 #   print(curr.val)
    curr= curr.next

def removenodes(node1):
    stack = []
    curr = node1
    while curr:

        while stack and curr.val > stack[-1].val:
            stack.pop()
        if stack:
            stack[-1].next = curr
        stack.append(curr)
        curr = curr.next
    return stack[0]


## remove adjacent elements
s = "foobar"
def removeadjacentelemenets(s):
    stack = []
    s = list(s)
    i = 0
    for c in s:
        if stack and stack[-1] == c:
                print(stack)
                stack.pop()
        else:
            stack.append(c)
    return stack


## Daily temperature
temp = [70, 73, 75, 71, 69, 72, 76, 73]
def temperature(temp):
    res = [0]*len(temp)
    stack = []
    curr = 0
    for i in range(len(temp)-1,-1,-1):
        while stack and stack[-1] < temp[-1]:
            stack.pop()
            curr+=1
        if stack:
            curr+=1
        stack.append(temp[i])
        print(stack)
        res[i] = curr
        curr = 0
    return res
