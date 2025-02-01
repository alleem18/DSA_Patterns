## Find non+duplicate\

nums = [0,0,1,1,1,2,2,3,3,4]
def twoPointers(nums):
    if len(nums) < 1:
        return 0
    l, r = 0, 1
    dup = 1
    while l < r and r < len(nums):
        if nums[l] == nums[r]:
            l+=1
            r+=1
        elif nums[l] != nums[r]:
            nums[l] = nums[r]
            dup+=1
            l+=1
            r+=1
    return dup, nums

##print(twoPointers(nums))


def sasa(nums):
    n = len(nums)
    new = [0] * n
    l, r = 0, n - 1
    pos = n - 1  # Start from the end of the new array

    while l <= r:
        left_sq = nums[l] ** 2
        right_sq = nums[r] ** 2
        if left_sq > right_sq:
            new[pos] = left_sq
            l += 1
        else:
            new[pos] = right_sq
            r -= 1
        pos -= 1  # Move to the next position to fill

    return new

# Example usage
#nums = [-2, -1, 0, 2, 3]
#print(sasa(nums))
"xyz##"
s1 = ["xywrrmu#p"]

def backspace(s1):
    l = r = len(s1)-1
    while l >= 0 and r >= 0 :
        if s1[l] == s1[r] == "#":
            l-=1
            r-=1
        l-=1
        elif s1[l] == "#" and s1[r] != "#":
            l-=1
            s1[l], s1[r] = s1[r], s1[l]
            r-=1
    return s1[:l]
#print(backspace(s1))


###













