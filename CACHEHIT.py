tests = int(input())
for test in range(tests):
    d = input().split()
    n = int(d[0])
    b = int(d[1])
    m = int(d[2])
    cRead = input().split()
    cRead = [int(i) for i in cRead]
    count = 0
    currCB = None
    for i in cRead:
        if currCB != (i//b):
            currCB = i//b
            count += 1
    print(count)


