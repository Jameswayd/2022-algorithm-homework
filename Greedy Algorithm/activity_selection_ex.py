def greedy_acitivty_selector(s, f):
    n = len(f)
    print ("The activities selected")
    i = 0
    for j in range(1,n):
        if s[j] >= f[i]:
            print (j,end=' ')
            i = j
# test 
s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
greedy_acitivty_selector(s, f)

print("")

def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        print (m,end=' ')
        r = recursive_activity_selector(s, f, m, n)
        return r
    else:
        return 0
# test
s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print ("The activities selected")
recursive_activity_selector(s, f, 0, len(s)-1)
