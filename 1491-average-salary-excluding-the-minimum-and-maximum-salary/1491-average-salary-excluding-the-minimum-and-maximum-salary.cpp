class Solution {
public:
    double average(vector<int>& salary) {
        int min_salary = 10000000;
        int max_salary = 0;
        int cum_sum = 0;
        int nb_employees = salary.size();
        int s = 0;
        for (int i=0; i<nb_employees; i++) {
            s = salary[i];
            cum_sum = cum_sum + s;
            if (s < min_salary) {
                min_salary = s;
            }
            if (s > max_salary) {
                max_salary = s;
            }
        }
        cum_sum = cum_sum - min_salary;
        cum_sum = cum_sum - max_salary;
        nb_employees = nb_employees - 2;
        double res;
        res = (double)cum_sum / (double)nb_employees;
        return res;
    }
};