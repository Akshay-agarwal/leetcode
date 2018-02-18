from collections import Counter
def CheckPerm(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    print(s1, s2, len(s1), len(s2))
    if len(s1) != len(s2):
        return False

    dict = Counter(s1)
    for char in s2:
        if dict[char] == 0:
            return False
        dict[char] -= 1
    return True

print(CheckPerm("aksh", "h a k s"))