from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = float('inf')
        for s in (1, -1):
            c = nums[0]
            if all(nums[i] == (s * i + c) % n for i in range(n)):
                if s == 1:
                    if c == 0:
                        cost = 0
                    else:
                        cost = min(n - c, c + 2)
                else:
                    d = (c + 1) % n
                    cost = min(d, (n - d) % n) + 1
                best = min(best, cost)
        return -1 if best == float('inf') else best