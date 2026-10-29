class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        chars = [1 << (ord(c) - 97) for c in s]
        par = [-1] * n
        par[0] = 0
        depth = [0] * n
        base = [0] * n
        tin = [0] * n
        tout = [0] * n
        ptr = [0] * n

        timer = 1
        tin[0] = 1
        base[0] = chars[0]
        stack = [0]
        while stack:
            u = stack[-1]
            if ptr[u] < len(adj[u]):
                v = adj[u][ptr[u]]
                ptr[u] += 1
                if v == par[u]:
                    continue
                par[v] = u
                depth[v] = depth[u] + 1
                base[v] = base[u] ^ chars[v]
                timer += 1
                tin[v] = timer
                stack.append(v)
            else:
                tout[u] = timer
                stack.pop()

        LOG = max(1, n.bit_length())
        up = [par[:]]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff >> k & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        size = n + 2
        bit = [0] * (size + 1)

        def bit_update(i, d):
            while i <= size:
                bit[i] ^= d
                i += i & -i

        def bit_query(i):
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def point(x):
            return base[x] ^ bit_query(tin[x])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                delta = chars[u] ^ new
                if delta:
                    bit_update(tin[u], delta)
                    bit_update(tout[u] + 1, delta)
                    chars[u] = new
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                mask = point(u) ^ point(v) ^ chars[w]
                ans.append(mask & (mask - 1) == 0)
        return ans