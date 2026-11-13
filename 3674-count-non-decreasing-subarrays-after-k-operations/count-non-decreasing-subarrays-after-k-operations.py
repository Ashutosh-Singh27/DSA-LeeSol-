from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        a = nums[::-1]
        dq = deque()
        cur = 0
        wsum = 0
        l = 0
        ans = 0
        for r, x in enumerate(a):
            cnt = 1
            while dq and dq[-1][0] <= x:
                v, c = dq.pop()
                cur -= v * c
                cnt += c
            dq.append([x, cnt])
            cur += x * cnt
            wsum += x
            while cur - wsum > k:
                dq[0][1] -= 1
                cur -= dq[0][0]
                wsum -= a[l]
                l += 1
                if dq[0][1] == 0:
                    dq.popleft()
            ans += r - l + 1
        return ans