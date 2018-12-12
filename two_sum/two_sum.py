class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_dict = {}
        for i in range(len(nums)):
        	num2 = target - nums[i]
        	if num2 in list_dict:
        		return [list_dict[num2], i]
        	else:
        		list_dict[nums[i]] = i