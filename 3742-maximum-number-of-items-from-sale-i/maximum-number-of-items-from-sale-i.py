class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        gain = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    gain[i] += 1

        order = sorted(range(n), key=lambda i: -items[i][1])  # price descending
        dp = [0] * (budget + 1)   # best value with cost <= b, 0/1 over processed items
        ans = 0

        for m in order:
            p = items[m][1]
            if p > budget:
                continue
            base = 1 + gain[m]
            left = budget - p
            for r in range(left + 1):
                ans = max(ans, dp[r] + base + (left - r) // p)
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + base)
        return ans