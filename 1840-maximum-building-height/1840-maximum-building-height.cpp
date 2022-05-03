using namespace std;

bool sortcol(const vector<int>& v1, const vector<int>& v2)
{
    return v1[0] < v2[0];
}
class Solution {
public:
    int calcMax(vector<int>& res1, vector<int>& res2) {
        int diff_idx = res2[0] - res1[0];
        int diff_h = res2[1] - res1[1];
        if (diff_h >= 0) {
            // we first egalize the size, then draw a parabola to reach max high
            int diff = diff_idx - diff_h;
            return this->max(res1[1], res2[1]) + (diff / 2);
        }
        int diff = diff_idx + diff_h;
        return this->max(res1[1], res2[1]) + (diff / 2);
    }
public:
    int min(int x, int y) {
      return (x < y) ? x : y;
    }
public:
    int max(int x, int y) {
      return (x < y) ? y : x;
    }
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        int N = restrictions.size();
        // int new_res[N+1][2];
        // new_res[0][0] = 0;
        // new_res[0][1] = 0;
        // for (int i=0; i<N; i++){
        //    new_res[i+1][0] = restrictions[i][0]-1;
        //    new_res[i+1][1] = restrictions[i][1];
        // }
        // sort(new_res, new_res+N+1);
        vector<vector<int>> new_res;
        new_res.push_back({0, 0});
        for (int i=0; i<N; i++) {
            new_res.push_back({restrictions[i][0]-1, restrictions[i][1]});
        }
        sort(new_res.begin(), new_res.end(), sortcol);
        
        // update the restrictions to reachable sizes (restriction due to height difference)
        for (int i=0; i<N; i++){
            new_res[i+1][1] = this->min(new_res[i+1][1], new_res[i][1]+(new_res[i+1][0]-new_res[i][0]));
        }
        for (int i=N; i>0; i--){
            new_res[i-1][1] = this->min(new_res[i-1][1], new_res[i][1] + (new_res[i][0] - new_res[i-1][0]));
        }

        int maximum = 0;
        int max_i = 0;
        for (int i=0; i<N; i++){
            max_i = this->calcMax(new_res[i], new_res[i+1]);
            maximum = this->max(maximum, max_i);
        }

        int nb_remaining_building = n - new_res[N][0] - 1;
        int max_last = nb_remaining_building + new_res[N][1];
        maximum = this->max(maximum, max_last);
        return maximum;
    }
};
