#10
N = int(input())
k = int(input())
def f(N, k):
    if N <= 0 or k <= 0:
        return 0
    a, b = 0, 1
    s = 0
    for i in range(1, k + N):
        if i >= k:
            s += a
        a, b = b, a + b
    return s
r = f(N, k)
print(r)