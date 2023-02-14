def cut_rod(prices, n):
    if n == 0:
        return 0
    q = -1
    for i in range(n):
        q = max(q, prices[i] + cut_rod(prices, n-i-1))
    return q


def top_down_cut_rod(prices, n ):
    memoized = [-1 for i in range(n)]
    if n == 0:
        return 0
    if memoized[n-1] >= 0:
        return memoized[n-1]
    q = -1
    for i in range(n):
        q = max(q, prices[i] + top_down_cut_rod(prices, n-i-1))
    memoized[n-1] = q
    return q

def extended_bottom_up_cut_rod(prices, n):
    memoized = [0 for i in range(n+1)] # the best sell money
    cut = [0 for i in range(n+1)]
    memoized[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            if q < prices[j-1] + memoized[i-j]:
                q = prices[j-1] + memoized[i-j]
                cut[i] = j
        memoized[i] = q
    return memoized[n], cut 


if __name__ == "__main__":
    # prices = [6, 10, 12, 15, 20, 23]
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    #n = int(input())  # n can not over len(prices)
    n = len(prices)
    print(cut_rod(prices, n))
    print(top_down_cut_rod(prices, n))
    print(extended_bottom_up_cut_rod(prices, n))
