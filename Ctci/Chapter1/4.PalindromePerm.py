def palinPerm(s):
    dict = {}
    i, j = 0, len(s) - 1
    while i <= j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        print(s[i], s[j])
        if i != j:

            dict[s[j].lower()] = dict.get(s[j].lower(), 0) + 1
        dict[s[i].lower()] = dict.get(s[i].lower(), 0) + 1
        i += 1
        j -= 1
    count = 0
    for key in dict.keys():
        if dict[key] % 2:
            count += 1
    print(dict)

    return count < 2

print(palinPerm("TACO act   ** acca"))