class Solution {
public:
    vector<string> recConvert(int num) {
        if (num >= 1000) {
            vector<string> res;
            for (int k=0; k<(num/1000); k++) {
                res.push_back("M");
            }
            vector<string> sub_res = this->recConvert(num % 1000);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 900) {
            vector<string> res;
            res.push_back("CM");
            vector<string> sub_res = this->recConvert(num - 900);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 500) {
            vector<string> res;
            res.push_back("D");
            vector<string> sub_res = this->recConvert(num - 500);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 400) {
            vector<string> res;
            res.push_back("CD");
            vector<string> sub_res = this->recConvert(num - 400);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 100) {
            vector<string> res;
            for (int k=0; k<(num/100); k++) {
                res.push_back("C");
            }
            vector<string> sub_res = this->recConvert(num % 100);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 90) {
            vector<string> res;
            res.push_back("XC");
            vector<string> sub_res = this->recConvert(num - 90);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 50) {
            vector<string> res;
            res.push_back("L");
            vector<string> sub_res = this->recConvert(num - 50);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 40) {
            vector<string> res;
            res.push_back("XL");
            vector<string> sub_res = this->recConvert(num - 40);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num >= 10) {
            vector<string> res;
            for (int k=0; k<(num/10); k++) {
                res.push_back("X");
            }
            vector<string> sub_res = this->recConvert(num % 10);
            for (int k=0; k<sub_res.size(); k++) {
                res.push_back(sub_res[k]);
            }
            return res;
        }
        if (num == 9) {
            vector<string> res;
            res.push_back("IX");
            return res;
        }
        if (num == 8) {
            vector<string> res;
            res.push_back("VIII");
            return res;
        }
        if (num == 7) {
            vector<string> res;
            res.push_back("VII");
            return res;
        }
        if (num == 6) {
            vector<string> res;
            res.push_back("VI");
            return res;
        }
        if (num == 5) {
            vector<string> res;
            res.push_back("V");
            return res;
        }
        if (num == 4) {
            vector<string> res;
            res.push_back("IV");
            return res;
        }
        if (num == 3) {
            vector<string> res;
            res.push_back("III");
            return res;
        }
        if (num == 2) {
            vector<string> res;
            res.push_back("II");
            return res;
        }
        if (num == 1) {
            vector<string> res;
            res.push_back("I");
            return res;
        }
        else {
            vector<string> res;
            res.push_back("");
            return res;
        }
    }
    string intToRoman(int num) {
        vector<string> l = this->recConvert(num);
        string res;
        for (auto &s : l) {
            res += s;
        }
        return res;
    }
};