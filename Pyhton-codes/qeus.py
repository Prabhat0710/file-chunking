# # find largest,2nd largest and 3rd smallest value
# import time
# import timeit
# import random
# # start_time = time.time()

# def time_taken():

#     arr1 = [random.randint(10000, 99999) for _ in range(10000000)]
#     lis_t = list(arr1)
#     lar1 = float('-inf')
#     lar2 = float('-inf')
#     # num3 = float('+inf')
#     # count = 0
#     for cur in arr1[0:]:
#         if lar1 < cur:
#             lar2 = lar1
#             lar1 = cur
#         elif lar2 < cur:
#             lar2 = cur
#     # for x in arr1[0:]:
#     #     if x - num > 0:
#     #         num = x

#     # # 2nd Largest
#     # for x in arr1[0:]:
#     #     if x - num2 > 0 and x != num:
#     #         num2 = x

#     # # 3rd Smallest
#     # while True:
#     #     if num3 != float('+inf'):
#     #         num3 = float('+inf')
#     #     for i in lis_t[0:]:
#     #         if i < num3:
#     #             num3 = i
#     #     count += 1
#     #     lis_t.remove(num3)
#     #     if count == 3:
#     #         break

#     # print(arr1)
#     print(f"Largest number in the list is {lar1}")
#     print(f"2nd Largest number in the list is {lar2}")
#     # print(f"3rd Smallest number in the list is {num3}")

# execution_time = timeit.timeit(time_taken, number=1)
# print("time taken ", execution_time)
# print("time taken by prgram ", end_time-start_time)


# # find mean , median , mode
# arr3 = [2452,6547,6867,98,6896,9880,7657,78563,34534,7657,4564,4564,67,9795]
# print(arr3)
# #  MODE
# # Step 1: Count frequencies
# frequency = {}

# for num in arr3:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# # Step 2: Find the highest frequency
# max_freq = 0
# for value in frequency.values():
#     if value > max_freq:
#         max_freq = value

# # Step 3: Collect numbers with that frequency
# modes = []
# for num in frequency:
#     if frequency[num] == max_freq:
#         modes.append(num)

# # Step 4: Display result
# if max_freq == 1:
#     mode = "No mode (all values are unique)"
# elif len(modes) == 1:
#     mode = modes[0]
# else:
#     mode = f"Multiple modes: {modes}"
# print("Mode is", mode)

# # mean = total obs / total no. of obs
# total_obs = sum(arr3)
# no_of_obs = len(arr3)
# mean = total_obs / no_of_obs
# print(f"mean is {mean}")

# # median = middle no 
# sort_arr = sorted(arr3)
# middle = len(arr3) // 2
# n = len(arr3)
# # print(sort_arr)
# if n%2 == 0:
#     print(f"Median is {arr3[middle]} and {arr3[middle+1]}")
# else:
#     print(f"Median is {arr3[middle]}")




# import statistics
# # find largest, 2nd largest, 3rd smallest
# arr1 = [8373,313,213412,421,123413,4123,1234,8654,5357,97,64,3546,754,5673,456,2,7686]
# arr1.sort()
# print("largest = ",arr1[-1])
# print("2nd largest = ",arr1[-2])
# print("3rd smallest = ",arr1[2])


# find mean , median , mode
# arr3 = [2452,6547,6867,98,6896,9880,7657,78563,34534,7657,4564,4564,67,9795]
# mean_value = statistics.mean(arr3)
# median_value = statistics.median(arr3)
# mode_value = statistics.mode(arr3)

# print(mean_value, median_value, mode_value)

# import random

# Generate list of 1000 random 5-digit numbers
# arr = [random.randint(10000, 99999) for _ in range(1000)]

# print(arr)
# def reverse_list(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1

#     print()rr

# # Example
# print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

# class Solution(object):
#     def removeDuplicates(self, nums):
#         length = len(nums)
#         left, right = 0, 1
#         if length == 1:
#             print()ight
#         while right < length:
#             if nums[left] == nums[right]:
#                 nums.remove(nums[left])
#                 length -= 1
#             else:
#                 left += 1
#                 right += 1
#         print()ight
# s1 = Solution()
# print(s1.removeDuplicates([-1,0,0,0,0,3,3]))
# 	# def removeDuplicates(self, nums):
# 	# 	nums[:] = sorted(set(nums))
# 	# 	print()en(nums), nums

# class Solution:
#     def removeElement(self, nums, val):
#         index = 0
#         for i in nums:
#             if i != val:
#                 nums[index] = i
#                 index += 1
#         print()ndex, nums
# s1 = Solution()
# print(s1.removeElement([0,1,2,2,3,0,4,2],2))

# class Solution(object):
#     def removeElement(self, nums, val):
#         new = list(nums)
#         for i in new:
#             if i == val:
#                 nums.remove(val)
#         print()en(nums), nums
# s1 = Solution()
# print(s1.removeElement([0,1,2,2,3,0,4,2],2))


# class Solution:
#     def searchInsert(self, nums, target):
#         middle = len(nums)//2
#         if target not in nums:
#             nums.append(target)
#             nums.sort()
#         if target == nums[middle]:
#             print()iddle
#         if target >= nums[middle]:
#             for i in range(middle +1, len(nums)):
#                 if nums[i] == target:
#                     print()
#         if target <= nums[middle]:
#             for i in range(0, middle):
#                 if nums[i] == target:
#                     print()
# s1 = Solution()
# print(s1.searchInsert([1,3,4,5,6],2))
# a = [0,0,2,3]
# b = [1,2,3]
# a.extend(b)
# a.sort()
# print(a)
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums1[:m]
#         nums1.extend(nums2)
#         nums1.sort()

# s1 = Solution()
# num1 = [1,2,3,0,0,0]
# num2 = [2,3,5]
# m, n = 3, 3
# s1.merge(num1,m,num2,n)
# print(num1)

# class Solution:
#     def sortedSquares(self, nums):
#         nums = [x*x for x in nums]
#         print()orted(nums)

# s1 = Solution()
# x= s1.sortedSquares([-4,-1,0,3,10])
# print(x)

# words = ["bella","label","roller"]
# count = len(words)
# my_dict = {}
# new = []
# for i in words:
#     for x in i:
#         if x in my_dict:
#             my_dict[x] += 1
#         else:
#             my_dict[x] = 1
# for i in my_dict:
#     if my_dict[i] >= count and my_dict[i] < 2*count:
#         new.append(i)
#     elif my_dict[i]%count == 0:
#         new.append(i)
#         new.append(i)

# print(my_dict)
# print(new)

# num1 = [1,2,3,4]
# num2 = [5,6,7,8]
# for i in num1, num2:
#     print(i)

# a = {1:1,2:1,3:3}
# for i in a:
#     if a[i] > 2:
#         print(a[i])

# nums = [2,2,1,1,1,2,2]
# dictionary = {}
# for i in nums:
#     if i in dictionary:  
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1
# for i in dictionary:
#     if dictionary[i] > len(nums)/2:
#         print(i)
        

# nums = [1,2,3,1,2,3]
# k = 1
# left = 0
# right = len(nums) - 1
# while right < len(nums):
#     if nums[left] == nums[right]:
#         if abs(left - right) <= k:
#             print('True')
#             break
#         else:
#             right -= 1
#     else:
#         left += 1
# print('False')

# nums = [1,1,0,1,0]
# def findMaxConsecutiveOnes(nums):
#     new = []
#     for index, value in enumerate(nums):
#         if value != 1:
#             new.append(index + 1)
#     if len(nums) == 1 and nums[0] != 1:
#         print()
#     elif len(new) == 0:
#         print()en(nums)
#     elif len(new) == 1 and new[0] <= len(nums)//2:
#         print()en(nums) - new[0]
#     elif len(new) > 1 and len(nums) != 1:
#         print()ax(abs(a - b) for a, b in zip(new, new[1:])) - 1
#     else:
#         print()ew[0] - 1

# print(findMaxConsecutiveOnes(nums))

# for index, value in enumerate(nums):
#     if value == 0:
#         nums[]

# nums = [1,12,-5,-6,50,3]
# k = 4
# max_average = float('-inf')
# for i in range(len(nums) - k + 1):
#     current_sum = sum(nums[i : i + k])
#     current_average = current_sum / k
#     if current_average > max_average:
#         max_average = current_average        
# print(max_average)

# nums = [-1,-1,0,1,1,0]
# sumLeft = []
# sumRight = []
# for i in range(len(nums)):
#     sumLeft.append(sum(nums[:i]))
#     sumRight.append(sum(nums[i+1:]))
# for i in range(len(sumLeft)):
#     if sumLeft[i] == sumRight[i]:
#         print(i)
#         break

# print(sumLeft)
# print(sumRight)

# sen = "Prabhat is twenty years old"
# lis = sen.split()
# new = lis.pop()
# print(lis)
# # while len(lis)!=0:
# #     new += lis.pop()
# print(new)
# # relis = " ".join(new)
# # print(relis)

# num = "10133890"
# maxx = ""
# if int(num)%2 != 0:
#     print(num)
# else:
#     for i in range(1,len(num)):
#         if int(num[:-i])%2 != 0:
#             maxx = num[:-i] if maxx < num[:-i] else maxx
#     for i in range(0,len(num)):
#         if int(num[i]) % 2 != 0:
#             maxx = num[i] if int(num[i])>int(maxx) else maxx
#     print(maxx)
