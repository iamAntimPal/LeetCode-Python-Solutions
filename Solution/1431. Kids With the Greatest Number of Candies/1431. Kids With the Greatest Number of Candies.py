from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies that any child currently has
        max_candies = max(candies)
      
        # Create a list of boolean values, where each value indicates whether a child
        # can have the greatest number of candies by adding the extraCandies to their current amount
        can_have_most_candies = [
            (child_candies + extraCandies) >= max_candies for child_candies in candies
        ]
      
        # Return the list of boolean values
        return can_have_most_candies
        