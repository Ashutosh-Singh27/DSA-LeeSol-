class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) &&
                    (j - i < 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }
        int ans = 0;
        int start = 0;
        for (int end = 0; end < n; end++) {
            for (int i = start; i <= end - k + 1; i++) {
                if (pal[i][end]) {
                    ans++;
                    start = end + 1;
                    break;
                }
            }
        }
        return ans;
    }
}