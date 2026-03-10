# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0, len(nums)):
#             for x in range(i+1,len(nums)):
#                 if nums[i] + nums[x] == target:
#                     return [i,x]

# num1 + num2 = target but num1 = target - num2 , num2 will be every number from list, after subraction if num1 in list num1,num2 return

class Solution:
    def twoSum(self, nums, target):
        for num in nums:
            num1 = target - num
            if num1 in nums:
                return [nums.indesx(num1),nums.index(num)]
            

class Solution:
    def twoSum(self, number_list, target):
        check = {}
        for i, num1 in enumerate(number_list):
            num2 = target - num1
            if num2 in check:
                return [check[num2],i]
            check[num2] = i

