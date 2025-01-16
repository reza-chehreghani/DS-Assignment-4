def dfs(adj, mark, v, des):
    if v == des:
        return []
    
    mark[v] = 1
    for u in adj[v]:
        if mark[u] == 0:
            path = dfs(adj, mark, u, des)
            if path != None:
                return [str(u)] + path
    return None


n = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v, u = input().split()
    v = int(v)
    u = int(u)
    adj[v].append(u)
    adj[u].append(v)

tour = list(map(int, input().split()))
tour = [1] + tour + [1]

ans = [str(1)]
for i in range(len(tour) - 1):
    mark = [0 for _ in range(n + 1)]
    ans += dfs(adj, mark, tour[i], tour[i + 1])

ans = ans[:-1]

if len(ans) > 2 * n - 2:
    print(-1)
else: #if len(ans) == 2 * n - 2:
    print(' '.join(ans))
# else:
#     print(' '.join(ans + ['1'] * (2 * n - 2 - len(ans))))
