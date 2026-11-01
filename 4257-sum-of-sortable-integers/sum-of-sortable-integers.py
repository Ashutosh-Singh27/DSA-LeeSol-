class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        pre = [0] * n
        for i in range(n - 1):
            pre[i + 1] = pre[i] + (nums[i] > nums[i + 1])
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = float('-inf')
            for s in range(0, n, k):
                e = s + k - 1
                c = pre[e] - pre[s] + (nums[e] > nums[s])
                if c > 1:
                    ok = False
                    break
                blk = nums[s:e + 1]
                if min(blk) < prev_max:
                    ok = False
                    break
                prev_max = max(blk)
            if ok:
                total += k
        return total