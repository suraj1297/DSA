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

        i = curr = 0
        j = len(nums) -1

        while curr <= j:
            if nums[curr] == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                i+=1
                curr+=1
            elif nums[curr] == 2:
                nums[j], nums[curr] = nums[curr], nums[j]
                j-=1
            else:
                cur+=1
                

Solution().sortColors([2,0,2,1,1,0])