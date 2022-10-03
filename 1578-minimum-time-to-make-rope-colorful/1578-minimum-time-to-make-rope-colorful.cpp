class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int total_time = 0;
        char streak_color = colors[0];  // current color
        int max_time = neededTime[0];  // max time of the current color
        int sum_time = neededTime[0];  // sum of time of the current color
        int streak = 1;  // number of balloons from the current color
        
        char c;
        for (int id_c=1; id_c<colors.length(); id_c++) {
            c = colors[id_c];
            if (c != streak_color) {  // if color changes
                streak_color = c;  // new color
                if (streak != 1) {  // if streak was k ballons>=2, remove k-1 ballons with min cost (so sum - max)
                    streak = 1;
                    total_time += sum_time - max_time;
                }
                max_time = neededTime[id_c];
                sum_time = neededTime[id_c];
            }
            else {  // update the streak
                streak++;
                max_time = std::max(max_time, neededTime[id_c]);
                sum_time += neededTime[id_c];
            }
        }
        // check the last streak
        if (streak != 1) {
            streak = 1;
            total_time += sum_time - max_time;
        }
        return total_time;
    }
};