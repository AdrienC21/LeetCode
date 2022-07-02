class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        horizontalCuts.push_back(0);
        horizontalCuts.push_back(h);
        sort(horizontalCuts.begin(), horizontalCuts.end());;
        verticalCuts.push_back(0);
        verticalCuts.push_back(w);
        sort(verticalCuts.begin(), verticalCuts.end());
        int max_h = 0;
        int max_w = 0;
        for (int i=0; i<(horizontalCuts.size() - 1); i++) {
            if ((horizontalCuts[i+1] - horizontalCuts[i]) > max_h) {
                max_h = (horizontalCuts[i+1] - horizontalCuts[i]);
            }
        }
        for (int i=0; i<(verticalCuts.size() - 1); i++) {
            if ((verticalCuts[i+1] - verticalCuts[i]) > max_w) {
                max_w = (verticalCuts[i+1] - verticalCuts[i]);
            }
        }
        long long int res = ((long long int)max_h * (long long int)max_w) % ((long long int)pow(10, 9) + 7);
        return (int) res;
    }
};