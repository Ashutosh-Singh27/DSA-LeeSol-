class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted((x * x for x in nums), reverse=True)
        k = (len(sq) + 1) // 2
        return sum(sq[:k]) - sum(sq[k:])