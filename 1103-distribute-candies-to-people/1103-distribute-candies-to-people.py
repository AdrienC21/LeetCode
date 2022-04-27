from math import sqrt
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        tot_sum = num_people * (num_people + 1) // 2
        delta = (tot_sum - num_people**2 / 2)**2 + 2 * num_people**2 * candies 
        k = int((-(tot_sum - num_people**2 / 2) + sqrt(delta)) / num_people**2)

        if k * tot_sum + k*(k-1) * num_people**2 / 2 >= candies:
            k -= 1
        res = []
        if k >= 1:
            facto_n = ((k - 1) * k) // 2
            base = facto_n * num_people
            remaining_candies = int(candies - (k * tot_sum + (k * (k-1)) * num_people**2 / 2))
            candies_remaining = (remaining_candies != 0)
            for i in range(num_people):
                to_append = (i + 1) * k + base
                if candies_remaining:
                    thresh = (k * num_people + i + 1)
                    if remaining_candies > thresh:
                        remaining_candies -= thresh
                        to_append += thresh
                    elif remaining_candies == thresh:
                        candies_remaining = False
                        remaining_candies = 0
                        to_append += thresh
                    else:
                        candies_remaining = False
                        thresh = remaining_candies
                        to_append += thresh
                        remaining_candies = 0
                res.append(int(to_append))
        else:
            remaining_candies = candies
            candies_remaining = (remaining_candies != 0)
            for i in range(num_people):
                if candies_remaining:
                    if remaining_candies > (i + 1):
                        remaining_candies -= (i + 1)
                        to_append = i + 1
                    elif remaining_candies == (i + 1):
                        candies_remaining = False
                        remaining_candies = 0
                        to_append = i + 1
                    else:
                        candies_remaining = False
                        to_append = remaining_candies
                        remaining_candies = 0
                else:
                    to_append = 0
                res.append(to_append)
        return res