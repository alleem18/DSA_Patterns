### first non repeating character

s = "applepie"
# output: a

def longestpalindrome(s):
    hm = {}
    for c in s:
        hm[c] = hm.get(c,0)+1

    count = 0
    odd = 0
    for i in hm.values():
        if i%2 == 0 :
            count = count + i
            print(count)
        else :
            count = count + i-1
            odd = 1

    print(count)
    return count+odd

###Ransom note:
Note = "apple"
Magazine = "pale"
def ransomnotes(Note, Magazine):

    hmapOfMagazine = {}
    for c in Magazine:
        hmapOfMagazine[c] = hmapOfMagazine.get(c,0)+1
    print(hmapOfMagazine)
    for c in Note:
        if not hmapOfMagazine.get(c) or hmapOfMagazine.get(c) == 0 :
            return False
        hmapOfMagazine[c]-=1
        print(hmapOfMagazine.get(c))
    return True

print(ransomnotes(Note, Magazine))