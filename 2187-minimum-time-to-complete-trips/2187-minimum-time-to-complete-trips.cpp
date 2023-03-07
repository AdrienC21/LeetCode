class Solution {
public:
    long long min_vector(vector<int>& time) {
        long long res = LONG_MAX;
        for (auto &t : time) {
            if (t < res) {
                res = t;
            }
        }
        return res;
    }

    long long minimumTime(vector<int>& time, int totalTrips) {
        long long i = 1;  // min number of time
        long long j = Solution::min_vector(time) * totalTrips;  // max number of time
        long long m;
        long long trips;
        while (i < j) {
            m = i + (j - i) / 2;
            trips = 0;  // count trips for that time
            for (auto &t : time) {
                trips += m / t;
            }
            if (trips >= totalTrips) {
                j = m;  // "at least", so j = m, not m - 1
            }
            else {
                i = m + 1;
            }
        }
        return i;
    }
};
