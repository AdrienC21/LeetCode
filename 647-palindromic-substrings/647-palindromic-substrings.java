class Solution {
    public int radiusSearch(String s, int lens, int i, int j) {
        int res = 0;
        while ((i >= 0) && (j < lens)) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            res++;
            // expand the radius!
            i--;
            j++;
        }
        return res;
    }
    public int countSubstrings(String s) {
        int lens = s.length();
        int res = 0;
        for (int i=0; i<lens; i++) {
            res += this.radiusSearch(s, lens, i, i);
            if (i < (lens - 1)) {  // search also palindrom with an even size
                res += this.radiusSearch(s, lens, i, i+1);
            }
        }
        return res;
    }
}
