import unittest


class CoinChange:
    def get_min_coins(self, coins: list[int], amount: int) -> int:
        max_val = amount + 1
        dp = [max_val] * (amount + 1)        
 
        dp[0] = 0        
 
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return -1 if dp[amount] > amount else dp[amount]
    

 

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.solver = CoinChange()

    def test_standard_case(self): 
        self.assertEqual(self.solver.get_min_coins([1, 2, 5], 11), 3)

    def test_no_solution(self):
        self.assertEqual(self.solver.get_min_coins([2], 3), -1)

    def test_amount_zero(self):
        self.assertEqual(self.solver.get_min_coins([1, 2, 5], 0), 0)

    def test_greedy_choice_fails(self):
        self.assertEqual(self.solver.get_min_coins([1, 5, 6, 9], 11), 2)

if __name__ == '__main__':
    unittest.main()