class Solution {
public:
    bool canWinNim(int n) {
        return not((n % 4) == 0);
    }
};