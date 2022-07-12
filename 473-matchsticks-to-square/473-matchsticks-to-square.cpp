class Solution {
private:  // variable to be accessed by the backtracking recursive function recSearch
    int side;
    bool recSearch(int i, int space_remaining, int sides_completed, vector<int>& matchsticks, int n) {
        if (sides_completed == 3) {  // all sides completed
            return true;
        }
        int num;
        bool res;
        while (i < n) {
            num = matchsticks[i];
            if (num > space_remaining) {  // skip this match
                i++;
                continue;
            }
            matchsticks[i] = side + 1;  // we will not use this matchstick
            if (num == space_remaining) {  // we completed a side
                res = recSearch(1, side, sides_completed+1, matchsticks, n);  // start at index 1 because first match is always placed on first side
            }
            else {
                res = recSearch(i+1, space_remaining-num, sides_completed, matchsticks, n);
            }
            if (res) {
                return true;
            }
            matchsticks[i] = num;  // put back the original value at index i

            bool sent = (i < n);
            if (sent) {
                sent = (matchsticks[i] == num);
            }
            while (sent) {  // process next value that is different !!
                i++;
                sent = (i < n);
                if (sent) {
                    sent = (matchsticks[i] == num);
                }
            }
        }
        return false;
    }
public:
    bool makesquare(vector<int>& matchsticks) {
        int s = 0;
        int n = matchsticks.size();
        for (int i=0; i<n; i++) {
            s += matchsticks[i];
        }
        if ((s % 4) != 0) {
            return false;
        }
        side = s / 4;
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());  // descending order
        if (matchsticks[0] > side) {  // at least a match is larger than the side
            return false;
        }
        return recSearch(0, side, 0, matchsticks, n);
    }
};
