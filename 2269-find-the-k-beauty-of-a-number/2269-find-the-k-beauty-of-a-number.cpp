class Solution {
public:
    int divisorSubstrings(int num, int k) {
        auto s = std::to_string(num);
        int n = s.length();
        int k_beauty = 0;
        int sub_int;
        std::string sub_str;
        for (int i=0; i<(n-k+1); i++) {
            sub_str = s.substr(i,k);
            sub_int = std::stoi(sub_str);
            if (sub_int and ((num % sub_int) == 0)) {
                k_beauty++;
            }
        }
        return k_beauty;
    }
};