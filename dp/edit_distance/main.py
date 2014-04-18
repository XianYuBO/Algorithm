def get_edit_distance(a, b):
    r = [[float('inf') for y in xrange(0, len(b) + 1)] for x in xrange(0, len(a) + 1)]
    for x in xrange(0, len(a) + 1):
        r[x][0] = x
    for y in xrange(0, len(b) + 1):
        r[0][y] = y
    for a_index, a_item in enumerate(a):
        for b_index, b_item in enumerate(b):
            if a_item == b_item:
                r[a_index + 1][b_index + 1] = r[a_index][b_index]
            else:
                r[a_index + 1][b_index + 1] = min((r[a_index][b_index],
                                                   r[a_index][b_index + 1], r[a_index + 1][b_index])) + 1

    return r[len(a)][len(b)]

if __name__ == "__main__":
    print get_edit_distance("kitten", "sitting")
