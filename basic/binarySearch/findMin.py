'''
Find Minimum in Rotated Sorted Array

Solution
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
   Hide Hint #1
Array was originally in ascending order. Now that the array is rotated,
there would be a point in the array where there is a small deflection
from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
   Hide Hint #2
You can divide the search space into two and see which direction to go.
Can you think of an algorithm which has O(logN) search complexity?
   Hide Hint #3
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.
'''
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    test_cases = [
        [3, 4, 5, 1, 2],  # Output: 1
        [4, 5, 6, 7, 0, 1, 2],  # Output: 0
        [11, 13, 15, 17],  # Output: 11
        [1],  # Output: 1 (Single element)
        [2, 1],  # Output: 1 (Smallest rotation possible)
        [5, 6, 7, 8, 9, 1, 2, 3],  # Output: 1
    ]
    solution = Solution()
    for case in test_cases:
        print(solution.findMin(case))