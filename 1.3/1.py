import sys


def main():
    arr = list(map(int, input().split()))
    prev = [None for _ in range(len(arr))]
    post = [None for _ in range(len(arr))]

    from_2 = None
    from_1 = None
    for i, num in enumerate(arr):
        if from_2 is not None: from_2 += 1
        if from_1 is not None: from_1 += 1
        if num == 2:
            from_2 = 0
        elif num == 1:
            if from_2 is not None:
                prev[i] = from_2
            from_1 = 0

    from_2 = None
    from_1 = None
    for i, num in enumerate(arr[::-1]):
        if from_2 is not None: from_2 += 1
        if from_1 is not None: from_1 += 1
        if num == 2:
            from_2 = 0
        elif num == 1:
            if from_2 is not None:
                post[i] = from_2
            from_1 = 0
    post = post[::-1]
    res = [0 for i in range(len(prev))]
    for i in range(len(prev)):
        if prev[i] == None and post[i] == None:
            res[i] = 0
            continue
        if prev[i] == None:
            res[i] = post[i]
            continue
        if post[i] == None:
            res[i] = prev[i]
            continue
        res[i] = min(prev[i], post[i])
    print(max(res))

if __name__ == '__main__':
    main()
