#Main Logic
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price  = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
#Input Logic
prices = list(map(int, input("Enter the prices:").split()))
#Output Logic
sol = Solution()
profit = sol.maxProfit(prices)
print("The maximum profit is", profit)

#R1