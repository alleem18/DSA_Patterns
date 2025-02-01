### binary to decimal

n = 7
def bintodec(n):
    stack = []
    while n > 0 :
        stack.append(str(n%2))
        n = n//2
    res = ""
    print(stack)
    while stack:
        res+=stack.pop()
    return res

## next greater element:
def nextLargerElement(arr):

    stack = []
    res = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res

def nextLargerElement2(arr):
    s = []
    res = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while s and s[-1] <= arr[i]:
            s.pop()

        if s:
            res[i] = s[-1]
        s.append(arr[i])  # Push the current element onto the stack

    return res

## sorting the array

stack = [5,1,6,2,7]
def sortingwithstack(stack):
    temp = []
    if not stack:
        return stack
    while stack:
        curr = stack.pop()
        while temp and temp[-1] > curr:
            stack.append(temp.pop())
        temp.append(curr)
    return temp
##simplify path

path = "/a/../../b/../c//.//"
def simplifypath(path):

    stack = path.split("/")
    print(stack)
    res = []
    for c in stack:
        if res and c =="..":
            res.pop()
        if c!="" and c!="." and c!="..":
            res.append(c)
            print(res,"res")
    print(res)
    return "/".join(res) if res else "/"
print(simplifypath(path))
