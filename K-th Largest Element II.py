class MyList:
    def __init__(self, numbers):
        self.numbers = numbers

    def kth_largest_element(self, k):
        sorted_numbers = sorted(self.numbers, reverse=True)
        
        if 1 <= k <= len(sorted_numbers):
            return sorted_numbers[k - 1]
        else:
            return None