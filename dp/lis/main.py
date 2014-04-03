def get_lis(lst):
    r = [1] * len(lst) or [0]
    for index, item in enumerate(lst):
        for j in xrange(0, index):
            if item >= lst[j] and r[index] < r[j] + 1:
                r[index] = r[j] + 1
    return max(r)

if __name__ == "__main__":
    print get_lis([1, -1, 2, -3, 4, -5, 6, -7])