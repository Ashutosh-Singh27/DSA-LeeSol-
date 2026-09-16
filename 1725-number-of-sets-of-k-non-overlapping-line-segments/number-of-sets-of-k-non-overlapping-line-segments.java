class Solution {
    public int numberOfSets(int n, int k) {
        long MOD = 1000000007L;
        long[][] dp = new long[k + 1][n];
        for (int i = 0; i < n; i++)
            dp[0][i] = 1;
        for (int j = 1; j <= k; j++) {
            long open = 0;
            for (int i = 1; i < n; i++) {
                open = (open + dp[j - 1][i - 1]) % MOD;
                dp[j][i] = (dp[j][i - 1] + open) % MOD;
            }
        }
        return (int) dp[k][n - 1];
    }
}