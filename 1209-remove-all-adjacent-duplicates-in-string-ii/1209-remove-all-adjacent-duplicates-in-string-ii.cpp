#include <stack>
using namespace std;
class Solution {
public:
    string removeDuplicates(string s, int k) {
        stack<int> stack;  // indices of the new letters
        stack.push(0);
        int n = s.length();
        int i = 1;  // indice of the letter in the word without duplicates
        int j = 1;  // indice of the letter in the original word (s)
        while (j < n) {
            s[i] = s[j];  // if we removed letters, need to update in real time the values in L
            if ((i == 0) or (s[i-1] != s[i])) {  // new character
                stack.push(i);
            }
            else if ((i - stack.top() + 1) == k) {  // k-duplicated characters
                i = stack.top() - 1;  // -1 because of the +1 after
                stack.pop();
            }
            i++;
            j++;  // go to next character
        }
        return s.substr(0, i);  // return the modified string (length of i)
    }
};