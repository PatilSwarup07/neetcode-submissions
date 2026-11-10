class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        p_price=0
        for sold in range(len(prices)):
            current_profit=prices[sold]-prices[p_price]
            profit=max(profit,current_profit)
            if prices[sold]<prices[p_price]:
                p_price=sold

        return profit


        