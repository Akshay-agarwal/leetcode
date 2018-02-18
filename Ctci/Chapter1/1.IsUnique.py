def isUnique(s):
    if len(s) > 128:
        return False

    charSet = [False for _ in range(128)]
    for char in s:
        val = ord(char)
        if charSet[val] == True:
            return False
        charSet[val] = True
    return True


print(isUnique("12345dfgh    j"))