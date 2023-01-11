class Solution:

    def quickSort(self, arr):
        if len(arr) < 2:
            return arr
        else:
            pivot = len(arr) // 2
            left = []
            right = []

            for i,v in enumerate(arr):
                if v <= arr[pivot] and i != pivot:
                    left.append(v)
                elif v>= arr[pivot] and i != pivot:
                    right.append(v)
            return self.quickSort(left) + [arr[pivot]] + self.quickSort(right)


    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        nums = self.quickSort(nums)
        print(nums)

Solution().sortColors([2,0,2,1,1,0])