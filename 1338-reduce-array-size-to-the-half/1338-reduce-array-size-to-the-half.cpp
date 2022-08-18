class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> freq;
        for (auto &num : arr) {
            freq[num]++;
        }
        vector<int> freq_list;
        for (auto &it : freq) {
            freq_list.push_back(it.second);
        }
        sort(freq_list.begin(), freq_list.end());
        int target = arr.size() / 2;
        int removed = 0;
        int count = 0;
        while (removed < target) {
            removed += freq_list.back();
            freq_list.pop_back();
            count++;
        }
        return count;
    }
};