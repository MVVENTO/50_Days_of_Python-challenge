#Name           :   Melissa A Vento
#Email          :   melissa.vento52@myhunter.cuny.edu
#Date           :   01/03/2022
#File Name      :   Small_k_length.py 
#Description    :   Interview question : Lambda function & Longest_Continuous_Increasing_Subsequence
#				:	674_Longest_Continuous_Increasing_Subsequence.py

#                          What is a lambda function?
#  A lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement. For Example:
# 	lambda arguments : expression
# 		The power of lambda is better shown when you use them as an anonymous function inside another function.

#	Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
#						 def myfunc(n):
#  							return lambda a : a * n



#		Q_674_Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
#	A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
#Example 1:

#Input: nums = [1,3,5,4,7]
#Output: 3
#Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
#Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
#4.
#Example 2:

#Input: nums = [2,2,2,2,2]
#Output: 1
#Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
#increasing.
#
#	Constraints:

#	1 <= nums.length <= 104
#	-109 <= nums[i] <= 109

   
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        ans = curr = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        return 