class Solution {
public:
    std::tuple<int, string, int> rom(int n, string s, int len_s) {
        if (len_s == 0) {
            return std::make_tuple(n, "", 0);
        }
        if (len_s == 1) {
            if (s[0] == 'M') {
                return std::make_tuple(n + 1000, "", 0);
            }
            if (s[0] == 'D') {
                return std::make_tuple(n + 500, "", 0);
            }
            if (s[0] == 'C') {
                return std::make_tuple(n + 100, "", 0);
            }
            if (s[0] == 'L') {
                return std::make_tuple(n + 50, "", 0);
            }
            if (s[0] == 'X') {
                return std::make_tuple(n + 10, "", 0);
            }
            if (s[0] == 'V') {
                return std::make_tuple(n + 5, "", 0);
            }
            if (s[0] == 'I') {
                return std::make_tuple(n + 1, "", 0);
            }
            else {
                return std::make_tuple(0, "", 0);  // raise error normally
            }
        }
        else {
            if (s[0] == 'M') {
                return this->rom(n + 1000, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "CM") {
                return this->rom(n + 900, s.substr(2), len_s - 2);
            }
            if (s[0] == 'D') {
                return this->rom(n + 500, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "CD") {
                return this->rom(n + 400, s.substr(2), len_s - 2);
            }
            if (s[0] == 'C') {
                return this->rom(n + 100, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "XC") {
                return this->rom(n + 90, s.substr(2), len_s - 2);
            }
            if (s[0] == 'L') {
                return this->rom(n + 50, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "XL") {
                return this->rom(n + 40, s.substr(2), len_s - 2);
            }
            if (s[0] == 'X') {
                return this->rom(n + 10, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "IX") {
                return this->rom(n + 9, s.substr(2), len_s - 2);
            }
            if (s[0] == 'V') {
                return this->rom(n + 5, s.substr(1), len_s - 1);
            }
            if (s.substr(0, 2) == "IV") {
                return this->rom(n + 4, s.substr(2), len_s - 2);
            }
            if (s[0] == 'I') {
                return this->rom(n + 1, s.substr(1), len_s - 1);
            }
            else {
                return std::make_tuple(0, "", 0);  // raise error normally
            }
        }
    }
    int romanToInt(string s) {
        int n;
        int l;
        tie(n, s, l) = this->rom(0, s, s.length());
        return n;
    }
};