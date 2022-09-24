class Solution {
public:
    int numberOfWays(string corridor) {
        vector<int> prods;
        int count_seat = 0;
        int total_count_seat = 0;
        int i = 0;
        int n = corridor.size();
        int current_dividor = 1;
        double mod = (pow(10, 9) + 7);
        while (i < n) {
            if (corridor[i] == 'S') {
                total_count_seat++;
                count_seat++;
                if (count_seat == 2) {
                    count_seat = 0;
                    i++;
                    current_dividor = 1;
                    while ((i < n) & (corridor[i] == 'P')) {
                        current_dividor++;
                        i++;
                    }
                    prods.push_back(current_dividor);
                }
                else {
                    i++;
                }
            }
            else {
                i++;
            }
        }

        if (prods.empty()) {
            return 0;
        }
        if ((total_count_seat % 2) == 1) {
            return 0;
        }
        if (prods.size() == 1) {
            return 1;
        }
        prods.pop_back();  // remove last one, because no two seats on the right

        double res = 1;
        while (!prods.empty()) {
            res *= prods.back();
            prods.pop_back();
            res = std::fmod(res, mod);
        }
        return (int) res;
    }
};