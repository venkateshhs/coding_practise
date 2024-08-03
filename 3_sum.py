def threeSum(nums):
    result_list =[]
    for index in range(len(nums)):
        value = nums[index]
        if value == 0:
            continue
        for next_index in range(index, len(nums)-1):
            if -value == (nums[next_index] + nums[next_index + 1]):
                print("Found", nums[index], nums[next_index], nums[next_index + 1])
                result_list.append([nums[index], nums[next_index], nums[next_index + 1]])

    return result_list




print(threeSum([[1,1,-2]]))


# Ideal Solution
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums.sort()  # Sort the array first

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for the first element

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate elements for the second element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate elements for the third element
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Move the left pointer to the right
                else:
                    right -= 1  # Move the right pointer to the left

        return result_list

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

