class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # code here
        new = list(zip(val, wt))
        new.sort(key=lambda x: x[0] / x[1], reverse=True)

        current = 0
        total = 0

        for value, weight in new:
            if current + weight <= capacity:
                current += weight
                total += value
            else:
                remain = capacity - current
                total += (value / weight) * remain
                break

        return total
