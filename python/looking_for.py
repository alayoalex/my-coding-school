def lookfor(a, b):
    def look(k, b):
        for v in b:
            if k == v:
                return True
        return False
    for k in a:
        if look(k, b) != True:
            b.append(k)
    print(b)


lookfor([1, 2, 3], [1, 4, 5])
