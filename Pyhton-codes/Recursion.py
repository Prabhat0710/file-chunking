'''def show(n):
    if n == 0: #it is called base case. Base case is the condition that stops the recursion. like in this case, when n is 0, the function will stop calling itself.
        return
    print(n)
    show(n - 1)

show(5)'''


## Factorial using recursion
# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive call     
# print(factorial(5))  

## print numbers from 1 to n
# def printNumbers(n):
#     if n < 1:
#         return
#     printNumbers(n-1)
#     print(n)
# printNumbers(20)

## print numbers from n to 1
# def printNumbers(n):
#     if n < 1:
#         return
#     print(n)
#     printNumbers(n-1)
# printNumbers(5)


## Sum of first n natural numbers
# def sum_number(n):
#     if n == 1:
#         return 1 
#     else:
#         return n + sum_number(n-1)
# result = sum_number(5)
# print(result)

## reverse the list
# def reverse(arr, n):
#     end = n
#     start = end - n
#     if start >= end:
#         return arr
#     else:
#         arr[start],arr[end-1] = arr[end-1], arr[start]
#         start += 1
#         end -= 1
#         return reverse(arr,end)
# print(reverse([1,2,3,4,5],5))

# def max_frequency(nums, k):
#     nums.sort()
#     left = 0
#     max_len = 0
#     current_sum = 0
#     for right in range(len(nums)):
#         current_sum += nums[right]
#         cost = (right - left + 1) * nums[right] - current_sum
#         while cost > k:
#             current_sum -= nums[left]
#             left += 1
#             cost = (right - left + 1) * nums[right] - current_sum
#         max_len = max(max_len, right - left + 1)        
#     return max_len

# my_nums = [20, 14, 1, 9]
# k_value = 2
# result = max_frequency(my_nums, k_value)
# print(f"The maximum possible frequency is: {result}")


# nums1 = [3,9,8,8,8, 4, 6, 7, 9, 9, 8]
# nums2 = [1, 5, 7, 8,8]

# len1 = len(nums1)
# len2 = len(nums2)
# if len1 > len2:
#     for i in nums2:
#         if i not in nums1:
#             nums1.append(i)
#     print(list(set(nums1)))
# else:
#     for i in nums1:
#         if i not in nums2:
#             nums1.append(i)
#     print(list(set(nums2)))
# print(sorted(set(nums1) | set(nums2)))

class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = 1
        while right!=len(nums)-1:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            elif nums[left] < nums[right]:
                right+=1
        return nums
    
c1 = Solution()
print(c1.sortColors([2,0,2,1,1,0]))