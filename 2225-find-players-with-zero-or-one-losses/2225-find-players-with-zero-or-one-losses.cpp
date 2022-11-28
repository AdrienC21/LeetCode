class Solution {
public:
    vector<int> diff(unordered_set<int>& set1, unordered_set<int>& set2) {
        vector<int> res;
        for (auto & k : set1) {
            if (set2.find(k) == set2.end()) {
                res.push_back(k);
            }
        }
        return res;
    }
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_set<int> players;
        unordered_set<int> has_lost;
        unordered_set<int> has_lost_twice;
        int w;
        int l;
        for (auto & m : matches) {
            w = m[0];
            l = m[1];
            players.insert(w);
            players.insert(l);
            if (has_lost.find(l) != has_lost.end()) {
                has_lost_twice.insert(l);
            }
            has_lost.insert(l);
        }
        vector<int> res1 = this->diff(players, has_lost);
        sort(res1.begin(), res1.end());
        vector<int> res2 = this->diff(has_lost, has_lost_twice);
        sort(res2.begin(), res2.end());
        vector<vector<int>> res;
        res.push_back(res1);
        res.push_back(res2);
        return res;
    }
};