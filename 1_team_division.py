def bfs(n, adj, color, impossible):
    mark = [0 for _ in range(n + 1)]

    for ver in range(1, n + 1):
        if mark[ver] == 0:
            color[ver] = 1
            mark[ver] = 1
            queue = [ver]
            while queue:
                v = queue.pop(0)
                num = 0
                for u in adj[v]:
                    if color[u] == color[v]:
                        num += 1
                    if mark[u] == 0:
                        color[u] = -color[v]
                        mark[u] = 1
                        queue.append(u)
                if num == len(adj[v]):
                    impossible = True
                mark[v] = 2


n, m = input().split()
n = int(n)
m = int(m)

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = input().split()
    u = int(u)
    v = int(v)
    adj[u].append(v)
    adj[v].append(u)


color = [0 for _ in range(n + 1)]
impossible = False

bfs(n, adj, color, impossible)

ans = []
for v in range(1, n + 1):
    if color[v] == 1:
        ans.append(str(v))

if impossible:
    print(-1)
else:
    print(len(ans))
    print(' '.join(ans))
