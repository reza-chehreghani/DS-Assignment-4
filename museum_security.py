n, m, k = list(map(int, input().split()))

vrtx = [(0, 0) for _ in range(k)]
adj = [[] for _ in range(k)]
is_right_down_light = False
for i in range(k):
    row, col = list(map(int, input().split()))
    vrtx[i] = (row, col)
    for j in range(i):
        if (vrtx[j][0] == row and (vrtx[j][1] - col == 1 or vrtx[j][1] - col == -1)) or ((vrtx[j][0] - row == 1 or vrtx[j][0] - row == -1) and vrtx[j][1] == col):
            adj[i].append((j, 0))
            adj[j].append((i, 0))
        elif (-2 <= vrtx[j][0] - row <= 2) or (-2 <= vrtx[j][1] - col <= 2):
            adj[i].append((j, 1))
            adj[j].append((i, 1))
    if row == n and col == m:
        is_right_down_light = True

vrtx_cost = [0 for _ in range(k)]
mark = [0 for _ in range(k)]
mark[0] = 1
queue = [0]
ans_cost = -1
while queue:
    v = queue.pop(0)
    for u, cost in adj[v]:
        if mark[u] == 0 or vrtx_cost[u] > vrtx_cost[v] + cost:
            mark[u] = 1
            vrtx_cost[u] = vrtx_cost[v] + cost

            if cost == 0:
                queue.insert(0, u)
            else:
                queue.append(u)

    if is_right_down_light:
        if vrtx[v][0] == n and vrtx[v][1] == m:
            ans_cost = vrtx_cost[v]
            break
    else:
        if (vrtx[v][0] == n - 1) or (vrtx[v][0] == n) or (vrtx[v][1] == m - 1) or (vrtx[v][1] == m):
            ans_cost = vrtx_cost[v] + 1
            break

print(ans_cost)
