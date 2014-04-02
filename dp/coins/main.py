def get_min_num_of_coins(coins_lst, money):
    r = [0] + [float('inf')] * money
    for i in xrange(1, money + 1):
        for j in coins_lst:
            if i - j >= 0 and r[i - j] + 1 < r[i]:
                r[i] = r[i - j] + 1
    return r[money]

if __name__ == "__main__":
    print get_min_num_of_coins([2, 3, 5], 567)