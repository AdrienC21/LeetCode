class Solution {
public:
    int pi(int n) {
        if (n <= 1) {
            return 0;
        }
        int count = 0;
        for (int num=2; num<(n+1); num++) {
            bool has_break = false;
            for (int i=2; i<num; i++) {
                if ((num % i) == 0) {
                    has_break = true;
                    break;
                }
            }
            if (not(has_break)) {
                count++;
            }
        }
        return count;
    }
public:
    double facto(int n, double mod) {
        double res = 1;
        for (int k=2; k<(n+1); k++) {
            res *= k;
            res = std::fmod(res, mod);
        }
        return res;
    }
public:
    double multiplyModulo(int a, int b, double c) {
        double result = 0;
        a = (int) std::fmod((double) a, c);
        b = (int) std::fmod((double) b, c);
        while(b) {
            if (b & 0x1) {
                result += a;
                result = std::fmod(result, c);
            }
            b >>= 1;
            if (a < c - a) {
                a <<= 1;
            } else {
                a -= (c - a);
            }
        }
        return result;
    }
public:
    int numPrimeArrangements(int n) {
        int pi_n = this->pi(n);
        double mod = (pow((double) 10, (double) 9) + 7);
        double res = this->multiplyModulo(this->facto(pi_n, mod), this->facto(n-pi_n, mod), mod);
        return (int) res;
    }
};