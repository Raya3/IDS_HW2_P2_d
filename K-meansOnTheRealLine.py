import numpy as np

np.set_printoptions(suppress=True)

inf = 999999
k = 3
a = [1, 2, 6, 7, 14, 18]
# k = 3
# a = [1, 2,5,7]
# k = 4
# a = [1, 2,5,7, 40,42,33,101,122,200]
n = len(a)
a = sorted(a)
M = np.array([[inf for j in range(k + 1)] for i in range(n + 1)],
             dtype="float")
P = np.array([[inf for j in range(k + 1)] for i in range(n + 1)])

for j in range(k + 1):
    M[0][j] = 0
    P[0][j] = 0

for j in range(1, k + 1):
    for i in range(1, n + 1):
        d = 0
        mean = 0
        for l in range(i, n + 1):
            offset = l - i
            d = d + (offset) / (offset + 1) * (a[l - 1] - mean)**2
            mean = (a[l - 1] + (offset) * mean) / (offset + 1)
            if M[i - 1][j - 1] + d < M[l][j]:
                M[l][j] = M[i - 1][j - 1] + d
                P[l][j] = i - 1
result = []
cut = n
j = k
while cut > 0:
    result.insert(0, a[P[cut][j]:cut])
    print(cut, P[cut][j])
    cut = P[cut][j]
    j -= 1
# print(M)
# print(P)
print(result)
