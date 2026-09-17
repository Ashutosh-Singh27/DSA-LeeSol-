class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] best = new int[n];
        Arrays.fill(best, Integer.MAX_VALUE);
        int left = 0;
        int sum = 0;
        int result = Integer.MAX_VALUE;
        int minLen = Integer.MAX_VALUE;
        for (int right = 0; right < n; right++) {
            sum += arr[right];
            while (sum > target) {
                sum -= arr[left];
                left++;
            }
            if (sum == target) {
                int currLen = right - left + 1;
                if (left > 0 && best[left - 1] != Integer.MAX_VALUE) {
                    result = Math.min(result, best[left - 1] + currLen);
                }
                minLen = Math.min(minLen, currLen);
            }
            best[right] = minLen;
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }
}