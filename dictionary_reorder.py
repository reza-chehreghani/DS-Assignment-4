from math import factorial
from itertools import permutations


n = int(input())

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
first_n_alphabet = english_alphabet[:n]

vrtx = [''.join(p) for p in permutations(first_n_alphabet)]
num = {vrtx[i]: i for i in range(factorial(n))}
adj = [[None for _ in range((n * (n - 1)) // 2)] for _ in range(factorial(n))]

for indx in range(factorial(n)):
    x = 0
    for i in range(n - 1):
        for j in range(i + 2, n + 1):
            adj[indx][x] = vrtx[indx][:i] + vrtx[indx][i: j][::-1] + vrtx[indx][j:]
            x += 1

# print(vrtx)
# print(adj)
t = int(input())
anss = [0 for _ in range(t)]

u, v = input().split()
des = [0 for _ in range(factorial(n))]
mark = [0 for _ in range(factorial(n))]

queue = [u]
des[num[u]] = 0
mark[num[u]] = 1
ans = 0
while queue:
    x = queue.pop(0)
    if x == v:
        ans = des[num[x]]
    for vtx in adj[num[x]]:
        if mark[num[vtx]] == 0:
            des[num[vtx]] = des[num[x]] + 1
            mark[num[vtx]] = 1
            queue.append(vtx)
anss[0] = ans

for i in range(1, t):
    up, vp = input().split()
    conv = {up[i]: u[i] for i in range(n)}
    v = ''.join([conv[vp[i]] for i in range(n)])
    anss[i] = des[num[v]]

print(*anss, sep='\n')

