class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        if ((m + n - 1) % 2 != 0) return false;
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;

        boolean[][][] visited = new boolean[m][n][m + n];
        return dfs(grid, 0, 0, 0, visited);
    }

    private boolean dfs(char[][] grid, int i, int j, int open, boolean[][][] visited) {
        int m = grid.length;
        int n = grid[0].length;

        if (i >= m || j >= n) return false;

        open += grid[i][j] == '(' ? 1 : -1;

        if (open < 0) return false;
        if (open > (m - i) + (n - j) - 2) return false;

        if (i == m - 1 && j == n - 1) return open == 0;

        if (visited[i][j][open]) return false;
        visited[i][j][open] = true;

        return dfs(grid, i + 1, j, open, visited) || dfs(grid, i, j + 1, open, visited);
    }
}