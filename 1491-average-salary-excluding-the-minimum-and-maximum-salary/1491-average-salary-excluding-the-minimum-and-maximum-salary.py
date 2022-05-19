class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = 10**7
        max_salary = 0
        cum_sum = 0
        nb_employees = len(salary)
        for s in salary:
            cum_sum += s
            if s < min_salary:
                min_salary = s
            if s > max_salary:
                max_salary = s
        cum_sum -= min_salary
        cum_sum -= max_salary
        nb_employees -= 2
        return cum_sum / nb_employees
