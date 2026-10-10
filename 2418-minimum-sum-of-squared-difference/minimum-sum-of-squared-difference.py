class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        m = max(abs(a - b) for a, b in zip(nums1, nums2))
        cnt = [0] * (m + 1)
        for a, b in zip(nums1, nums2):
            cnt[abs(a - b)] += 1

        if sum(i * cnt[i] for i in range(m + 1)) <= k:
            return 0

        top = m
        while top > 0 and k > 0:
            c = cnt[top]
            if c == 0:
                top -= 1
                continue
            if c <= k:
                k -= c
                cnt[top - 1] += c
                cnt[top] = 0
                top -= 1
            else:
                cnt[top] -= k
                cnt[top - 1] += k
                k = 0

        return sum(i * i * cnt[i] for i in range(m + 1))