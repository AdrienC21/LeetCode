class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.push_back(0);  // add the top floor
        int n = cost.size();
        deque<int> d;
        d.push_back(n-1);  // for every i, store the reacheable position (here within two steps) with the lowest cumulative cost
        bool sent;
        for (int i=(n-2); i>=0; i--) {
            if ((d.front() - i) > 2) {  // max two steps
                d.pop_front();
            }
            cost[i] += cost[d.front()];
            // sentinelle value for the while loop
            sent = !(d.empty());
            if (sent) {
                sent = (cost[d.back()] >= cost[i]);
            }
            while (sent) {
                d.pop_back();
                sent = !(d.empty());
                if (sent) {
                    sent = (cost[d.back()] >= cost[i]);
                }
            }
            d.push_back(i);
        }
        // return min score (start at 0 or 1st step)
        if (cost[0] < cost[1]) {
            return cost[0];
        }
        return cost[1];
    }
};
