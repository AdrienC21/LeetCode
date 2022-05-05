class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // let's use two pointers
        int pleft = 0;
        int pright = numbers.size() - 1;
        int nbleft = numbers[pleft];
        int nbright = numbers[pright];
        int s;
        vector<int> res;
        while (pleft < pright) {
            s = nbleft + nbright;
            if (s < target) {
                pleft++;
                nbleft = numbers[pleft];
            }
            else if (s > target) {
                pright--;
                nbright = numbers[pright];
            }
            else {
                res.push_back(pleft+1);
                res.push_back(pright+1);
                return res;
            }
        }
        res.push_back(-1);
        res.push_back(-1);
        return res;
    }
};