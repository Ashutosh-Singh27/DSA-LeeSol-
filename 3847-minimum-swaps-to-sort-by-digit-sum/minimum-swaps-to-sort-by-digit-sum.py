class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def ds(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        target = sorted(nums, key=lambda x: (ds(x), x))
        pos = {v: i for i, v in enumerate(target)}

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                length += 1
            swaps += length - 1
        return swaps