def lock(s):
    stack = []
    lock_set = set()
    for i in range(len(s)):
        entry = s[i].split()
        lock_type = entry[0]
        if len(stack) == 0 and lock_type == "Release":
            return i + 1
        lock_num = int(entry[1])
        if lock_type == "Acquire":
            if lock_num not in lock_set:
                stack.append(lock_num)
                lock_set.add(lock_num)
            else:
                return i + 1
        else:
            if stack.pop() == lock_num:
                lock_set.remove(lock_num)
            else:
                return i + 1
    return 0 if len(lock_set) == 0 else len(s) + 1


a = lock(["Acquire 45"])
print(a)
