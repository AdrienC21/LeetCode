class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0) {
            return 0;
        }
        int n = needle.size();
        int h = haystack.size();
        if (n > h) {
            return -1;
        }
        int i = 0;
        bool found = true;
        int k;
        while (i <= (h-n)) {
            found = true;
            k = i;
            while ((found) && (k < (i+n))) {
                if (haystack[k] != needle[k-i]) {
                    found = false;
                }
                k++;
            }
            if (found) {
                return i;
            }
            i++;
        }
        return -1;
    }
};