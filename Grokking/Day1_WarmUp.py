####
"Warmup"

nums = [1,2,3,4,]
def containsdup(nums):
    h = set()
    for i in range(len(nums)):
        if nums[i] in h:
            return True
        h.add(nums[i])

    return False

##print(containsdup(nums))


### Reverse Vowels

s = "hello"

def reversev(s):
    vs = list("aeiou")
    s = list(s)
    l, r = 0, len(s)-1

    while l <= r:
        if s[l].lower() in vs and s[r].lower() in vs:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        if s[l].lower() not in vs:
            l+=1
        if  s[r].lower() not in vs:
            r-=1

    return "".join(s)

###print(reversev(s))


## valid anagram

def isAnagram( s: str, t: str):
    if len(s) != len(t):
        return False
    freq_map = {}

    for i in range(len(s)):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    print(freq_map)
    for i in range(len(s)):
        if t[i] in freq_map:
            freq_map[t[i]] -= 1


    print(freq_map)

    res = 0
    for i in freq_map:
        if freq_map[i] != 0:
            return False
    return True

##print(isAnagram("aacc", "ccac"))

### Shortest word distance
words = ["a", "c", "d", "b", "a"]

word1 = "a"
word2 = "b"

def swd(words, word1, word2):
    w1 = -1
    w2 = -1
    res = len(words)
    for i in range(len(words)):
        if words[i] == word1:
            w1 = i
        if words[i] == word2:
            w2 = i
        if w1 != -1 and w2 != -1:
            res = min(res, abs(w2-w1))

    return res

#print(swd(words, word1, word2))


## Number of god pairs
nums = [1,1,1,1]

def ngp(nums):
    hmap = {}
    pc = 0
    for i in range(len(nums)):
        if nums[i] in hmap:
            hmap[nums[i]]+=1
            pc += hmap[nums[i]] - 1

        else:
            hmap[nums[i]] = 1


    return pc

##print(ngp(nums))



## sqrt

def sqrt(n):

    if n < 2 :
        return n

    l, r = 2, (n)//2
    mid = 0
    num = 0
    while l <= r:
        mid = l+(r-l)//2
        num = mid * mid
        if num > n :
            r = mid - 1
        elif num < n:
            l = mid + 1
        else:
            return mid
    return r

#print(sqrt(8))



### rotate array

arr = [1,2,3,4,5,6]
k = 3

def reverse(arr, l , r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    return arr
def rotate(arr,k):
    reverse(arr, 0, k-1)
    print(arr)
    reverse(arr,k, len(arr)-1)
    print(arr)
    reverse(arr,0, len(arr)-1)
    print(arr)
    return arr
#print(rotate(arr,k))







## Reverse a string
s = "Hello, World!"



def reverseString(s):
    stack = list(s)
    s = []
    while stack:
        s += stack.pop()

    return s


#print(reverseString(s))
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    res = []
    prev, curr = 0, 1
    for i in range(n+1):
        res.append(prev)
        next = curr + prev
        prev = curr
        curr = next

    return res

def recfib(n):
    if n == 0 or n == 1:
        return n
    return recfib(n-1) + recfib(n-2)

print(recfib(10))
# Example usage:
print(fibonacci_iterative(10))  # Output: 55




