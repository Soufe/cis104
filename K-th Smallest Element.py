class MyList:
    def __init__(self, nums):
        self.nums = nums

    def add(self, val):
        self.nums.append(val)

class YourList(MyList):
    def __init__(self, nums):
        super().__init__(nums)

    def kth_smallest_element(self, k):
        sorted_nums = sorted(self.nums)
        if 1 <= k <= len(sorted_nums):
            return sorted_nums[k - 1]
        else:
            raise ValueError("Invalid value of k")