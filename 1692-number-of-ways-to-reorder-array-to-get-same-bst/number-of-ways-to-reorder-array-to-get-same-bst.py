class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def count(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            result = comb[len(left) + len(right)][len(left)]
            result = result * count(left) % MOD
            result = result * count(right) % MOD
            return result

        return (count(nums) - 1) % MOD