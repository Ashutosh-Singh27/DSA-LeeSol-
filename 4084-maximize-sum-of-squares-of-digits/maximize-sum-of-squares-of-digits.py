class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines = sum // 9
        rem = sum % 9
        res = "9" * nines
        if nines < num:
            res += str(rem)
            res += "0" * (num - nines - 1)
        return res