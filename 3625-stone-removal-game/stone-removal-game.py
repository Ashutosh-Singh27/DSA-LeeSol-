class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = True
        take = 10
        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice = not alice
        # alice now indicates whose turn it is when play stops
        return not alice