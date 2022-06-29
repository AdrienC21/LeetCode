class Solution {
public:
    static bool cmp(vector<int>& x, vector<int>& y) {
        if (x[1] == y[1]) {
            if (not(x[1])) {
                return x[0] < y[0];
            }
            return y[0] < x[0];
        }
        return x[1] < y[1];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        // then, add the people iteratively
        vector<vector<int>> res;
        // first, people with no person higher than them in front
        // sorted by increasing height
        bool break_called = false;
        vector<int> p;
        int j = 0;
        while (j < people.size()) {
            p = people[j];
            if (not(p[1])) {
                res.push_back(p);
            }
            else {
                break_called = true;
                break;
            }
            j++;
        }
        if (not(break_called)) {  // if no people remaining, return
            return res;
        }

        // then the others. We insert them at the beginning, then move to the right until we reached k people taller in front of them
        int h;
        int k;
        int index;
        int count_larger;
        for (int i=j; i<people.size(); i++) {
            p = people[i];
            h = p[0];
            k = p[1];
            index = 0;  // index in res
            count_larger = 0;  // people taller than pi in front of pi
            while ((count_larger < k) & (index < res.size())) {
                if (h <= res[index][0]) {
                    count_larger++;
                }
                index++;
            }
            res.insert(res.begin() + index, p);
        }
        return res;
    }
};