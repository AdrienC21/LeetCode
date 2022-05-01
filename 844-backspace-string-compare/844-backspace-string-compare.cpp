#include<stdio.h>
#include<string.h>
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> Ls;
        stack<char> Lt;
        int ns = s.length();
        int nt = t.length();
        for (int i=0; i<ns; i++) {
            if (s[i] == '#') {
                if (not(Ls.empty())) {
                    Ls.pop();
                }
            }
            else {
                Ls.push(s[i]);
            }
            
        }
        for (int i=0; i<nt; i++) {
            if (t[i] == '#') {
                if (not(Lt.empty())) {
                    Lt.pop();
                }
            }
            else {
                Lt.push(t[i]);
            }
            
        }
        if (Ls.size() != Lt.size()) {
            return false;
        }
        else{
            bool res = true;
            int n = Ls.size();
            int i = 0;
            while (res & (i < n)) {
                res = (Ls.top() == Lt.top());
                Ls.pop();
                Lt.pop();
                i++;
            }
            return res;
        }
    }
};