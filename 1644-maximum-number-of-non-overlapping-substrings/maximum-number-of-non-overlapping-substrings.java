class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        List<int[]> intervals = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) continue;
            int start = first[i];
            int end = last[i];
            boolean valid = true;
            int j = start;
            while (j <= end) {
                int c = s.charAt(j) - 'a';
                if (first[c] < start) {
                    valid = false;
                    break;
                }
                if (last[c] > end) end = last[c];
                j++;
            }
            if (valid) intervals.add(new int[]{start, end});
        }
        intervals.sort((a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);
        List<String> res = new ArrayList<>();
        int prevEnd = -1;
        for (int[] iv : intervals) {
            if (iv[0] > prevEnd) {
                res.add(s.substring(iv[0], iv[1] + 1));
                prevEnd = iv[1];
            }
        }
        return res;
    }
}