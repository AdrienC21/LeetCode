class Solution {
public:
    // flow from atlantic and pacific!
    std::tuple<int, int> int_to_tuple(int number, int n) {
        if (number == -1) {
            return std::make_tuple(0, -1);
        }
        if (number == -2) {
            return std::make_tuple(0, -2);
        }
        int k = number / n;
        int l = number % n;
        return std::make_tuple(k, l);
    }
    
    int tuple_to_int(std::tuple<int, int> t, int n) {
        int k;
        int l;
        tie(k, l) = t;
        if (l == -1) {
            return -1;
        }
        if (l == -2) {
            return -2;
        }
        return k * n + l;
    }
    
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        unordered_map<int, vector<std::tuple<int, int>>> graph;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                for (int h=-1; h<2; h+=2) {
                    if (((j + h) >= 0) and ((j + h) < n)) {
                        if (heights[i][j+h] > heights[i][j]) {
                            graph[this->tuple_to_int(std::make_tuple(i, j), n)].push_back(std::make_tuple(i, j+h));
                        }
                        else {
                            if (heights[i][j+h] < heights[i][j]) {
                                graph[this->tuple_to_int(std::make_tuple(i, j+h), n)].push_back(std::make_tuple(i, j));
                            }
                            else {
                                graph[this->tuple_to_int(std::make_tuple(i, j), n)].push_back(std::make_tuple(i, j+h));
                                graph[this->tuple_to_int(std::make_tuple(i, j+h), n)].push_back(std::make_tuple(i, j));
                            }
                        }
                    }
                }
                for (int v=-1; v<2; v+=2) {
                    if (((i + v) >= 0) and ((i + v) < m)) {
                        if (heights[i+v][j] > heights[i][j]) {
                            graph[this->tuple_to_int(std::make_tuple(i, j), n)].push_back(std::make_tuple(i+v, j));
                        }
                        else {
                            if (heights[i+v][j] < heights[i][j]) {
                                graph[this->tuple_to_int(std::make_tuple(i+v, j), n)].push_back(std::make_tuple(i, j));
                            }
                            else {
                                graph[this->tuple_to_int(std::make_tuple(i, j), n)].push_back(std::make_tuple(i+v, j));
                                graph[this->tuple_to_int(std::make_tuple(i+v, j), n)].push_back(std::make_tuple(i, j));
                            }
                        }
                    }
                }
            }
        }
        // pacific = std::make_tuple(0, -1)
        // atlantic = std::make_tuple(0, -2)
        for (int i=0; i<m; i++) {
            graph[this->tuple_to_int(std::make_tuple(0, -1), n)].push_back(std::make_tuple(i, 0));
            graph[this->tuple_to_int(std::make_tuple(0, -2), n)].push_back(std::make_tuple(i, n-1));
        }
        for (int j=1; j<n; j++) {
            graph[this->tuple_to_int(std::make_tuple(0, -1), n)].push_back(std::make_tuple(0, j));
            graph[this->tuple_to_int(std::make_tuple(0, -2), n)].push_back(std::make_tuple(m-1, j-1));
        }
        unordered_set<int> reached_pacific;
        unordered_set<int> reached_atlantic;
        
        unordered_set<int> visited;
        stack<std::tuple<int, int>> to_visit;
        to_visit.push(std::make_tuple(0, -1));
        std::tuple<int, int> u;
        std::tuple<int, int> v;
        int int_u;
        int int_v;
        while (!to_visit.empty()) {
            u = to_visit.top();
            to_visit.pop();
            int_u = tuple_to_int(u, n);
            if (visited.find(int_u) == visited.end()) {
                visited.insert(int_u);
                reached_pacific.insert(int_u);
                for (auto &v : graph[int_u]) {
                    int_v = tuple_to_int(v, n);
                    if (visited.find(int_v) == visited.end()) {
                        to_visit.push(v);
                    }
                }
            }
        }
        
        visited.clear();
        while (!to_visit.empty()) {
            to_visit.pop();
        }
        to_visit.push(std::make_tuple(0, -2));
        while (!to_visit.empty()) {
            u = to_visit.top();
            to_visit.pop();
            int_u = tuple_to_int(u, n);
            if (visited.find(int_u) == visited.end()) {
                visited.insert(int_u);
                reached_atlantic.insert(int_u);
                for (auto &v : graph[int_u]) {
                    int_v = tuple_to_int(v, n);
                    if (visited.find(int_v) == visited.end()) {
                        to_visit.push(v);
                    }
                }
            }
        }
        
        int i;
        int j;
        vector<vector<int>> res;
        vector<int> sub_res;
        for (auto &t : reached_pacific) {
            if (reached_atlantic.find(t) != reached_atlantic.end()) {
                tie(i, j) = int_to_tuple(t, n);
                vector<int> sub_res;
                sub_res.push_back(i);
                sub_res.push_back(j);
                res.push_back(sub_res);
            }
        }
        return res;
    }
};