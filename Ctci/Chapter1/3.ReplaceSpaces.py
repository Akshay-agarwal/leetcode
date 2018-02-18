def urlify(s, i, j):
    s = list(s)
    while i > 0:
        if s[i] != " ":
            s[j:j+1] = s[i]
            j -= 1
        else:
            s[j-2:j+1] = "%20"
            j -= 3
        i -= 1

    print("".join(s))

urlify("My name is Snith      ",15, 21)
