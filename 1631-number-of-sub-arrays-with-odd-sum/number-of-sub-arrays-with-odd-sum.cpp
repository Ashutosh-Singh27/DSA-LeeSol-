class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1000000007;
        long long odd = 0, even = 1, ans = 0;
        int prefix = 0;
        for (int x : arr) {
            prefix ^= (x & 1);
            if (prefix) {
                ans += even;
                odd++;
            } else {
                ans += odd;
                even++;
            }
            ans %= MOD;
        }
        return (int)ans;
    }
};