from typing import List
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        # if len(nums) > 1:
        #     length = len(nums)
        #     middle = length // 2
        #     left_arr = nums[:middle]
        #     right_arr = nums[middle:]
        #
        #     self.sortColors(left_arr)
        #     self.sortColors(right_arr)
        #
        #     i = 0  #left index
        #     j = 0  #right index
        #     k = 0  # merged index
        #     while i < len(left_arr) and j < len(right_arr):
        #         if left_arr < right_arr:
        #             nums[k] = left_arr[i]
        #             i += 1
        #         else:
        #             nums[k] = right_arr[j]
        #
        #         k += 1


solution = Solution()

# Define the nums list
nums = [0, 2, 4, 1, 0]

# Call the sortColors method with nums
solution.sortColors(nums)
print(nums)