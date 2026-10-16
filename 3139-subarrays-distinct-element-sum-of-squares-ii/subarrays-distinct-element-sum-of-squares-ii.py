class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        s = [0] * (2 * size)
        q = [0] * (2 * size)
        lz = [0] * (2 * size)
        ln = [1] * (2 * size)
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2 * i] * 2

        def apply(node, k):
            q[node] += 2 * k * s[node] + k * k * ln[node]
            s[node] += k * ln[node]
            lz[node] += k

        def update(node, lo, hi, a, b):
            if a <= lo and hi <= b:
                apply(node, 1)
                return
            if lz[node]:
                apply(2 * node, lz[node])
                apply(2 * node + 1, lz[node])
                lz[node] = 0
            mid = (lo + hi) // 2
            if a <= mid:
                update(2 * node, lo, mid, a, b)
            if b > mid:
                update(2 * node + 1, mid + 1, hi, a, b)
            s[node] = s[2 * node] + s[2 * node + 1]
            q[node] = q[2 * node] + q[2 * node + 1]

        last = {}
        ans = 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, r)
            last[x] = r
            ans += q[1]
        return ans % MOD