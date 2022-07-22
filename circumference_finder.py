def circ(c):
    c *= 12
    count = 0
    while c > 0.01:
        print(c)
        c = c/2
        count += 1
    return c, count

print(circ(8))
