class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables with infinity which will
        # represent the smallest and middle numbers of the triplet.
        smallest = float('inf')
        middle = float('inf')

        # Iterate over the list of numbers.
        for num in nums:
            # If current number is greater than the middle number,
            # an increasing triplet exists.
            if num > middle:
                return True
          
            # If current number is less than or equal to the smallest,
            # update the smallest number to be the current number.
            if num <= smallest:
                smallest = num
            # Otherwise, if the current number is between the smallest
            # and the middle, update the middle number.
            else:
                middle = num

        # Return False if no increasing triplet is found.
        return False