import java.util.*;

class Solution {
    int k;
    int n;
    int[] arr;
    int[][][] cnt;
    int[] prod;
    int lastProd;
    int identity;

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.k = k;
        this.n = nums.length;
        this.arr = nums.clone();
        this.identity = 1 % k;
        cnt = new int[4 * n][k][k];
        prod = new int[4 * n];
        build(1, 0, n - 1);

        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];
            arr[idx] = val;
            update(1, 0, n - 1, idx);
            int[][] r = queryRange(1, 0, n - 1, start, n - 1);
            res[i] = r[identity][x];
        }
        return res;
    }

    void setLeaf(int node, int l) {
        int a = arr[l] % k;
        for (int rr = 0; rr < k; rr++) {
            for (int c = 0; c < k; c++) cnt[node][rr][c] = 0;
            cnt[node][rr][(rr * a) % k] = 1;
        }
        prod[node] = a;
    }

    void build(int node, int l, int r) {
        if (l == r) {
            setLeaf(node, l);
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
        mergeUp(node);
    }

    void mergeUp(int node) {
        int left = 2 * node, right = 2 * node + 1;
        int pl = prod[left];
        for (int rr = 0; rr < k; rr++) {
            int rMap = (rr * pl) % k;
            for (int c = 0; c < k; c++) {
                cnt[node][rr][c] = cnt[left][rr][c] + cnt[right][rMap][c];
            }
        }
        prod[node] = (pl * prod[right]) % k;
    }

    void update(int node, int l, int r, int idx) {
        if (l == r) {
            setLeaf(node, l);
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx);
        else update(2 * node + 1, mid + 1, r, idx);
        mergeUp(node);
    }

    int[][] combine(int[][] cntA, int prodA, int[][] cntB, int prodB, int[] outProd) {
        if (cntA == null) {
            outProd[0] = prodB;
            return cntB;
        }
        if (cntB == null) {
            outProd[0] = prodA;
            return cntA;
        }
        int[][] res = new int[k][k];
        for (int rr = 0; rr < k; rr++) {
            int rMap = (rr * prodA) % k;
            for (int c = 0; c < k; c++) {
                res[rr][c] = cntA[rr][c] + cntB[rMap][c];
            }
        }
        outProd[0] = (prodA * prodB) % k;
        return res;
    }

    int[][] queryRange(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) {
            lastProd = -1;
            return null;
        }
        if (ql <= l && r <= qr) {
            lastProd = prod[node];
            return cnt[node];
        }
        int mid = (l + r) / 2;
        int[][] leftRes = queryRange(2 * node, l, mid, ql, qr);
        int leftProd = lastProd;
        int[][] rightRes = queryRange(2 * node + 1, mid + 1, r, ql, qr);
        int rightProd = lastProd;
        int[] outProd = new int[1];
        int[][] combined = combine(leftRes, leftProd, rightRes, rightProd, outProd);
        lastProd = outProd[0];
        return combined;
    }
}