class Solution:

    def getKElements(self, nums, k):
        
        if len(nums) == k:
            return nums
        else:
            mid = len(nums) - 1
            sub = [i for i in nums if i > nums[mid]]

            return self.getKElements(sub, k)

    def findKthLargest(self, nums, k):


        return self.getKElements(nums, k)[0]
            

print(Solution().findKthLargest([3,2,1,5,6,4], 2))