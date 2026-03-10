# # Pattern 1
# num = 1
# while num < 6:
#     num += 1
#     for i in range(0,5):
#         print("*",end =" ")
#     print()


# # Pattern 2
# nums = 1
# while nums < 6:
#     nums += 1
#     for i in range(0,nums-1):
#         print("*",end =" ")
#     print()


# # Pattern 3
# nums = 1
# while nums < 6:
#     nums += 1
#     for i in range(1,nums):
#         print(i,end =" ")
#     print()


# # Pattern 4
# nums = 1
# while nums < 6:
#     nums += 1
#     for i in range(0,nums-1):
#         print(nums-1,end =" ")
#     print()


# # Pattern 5
# nums = 6
# while nums > 1:
#     nums -= 1
#     for i in range(0,nums):
#         print("*",end =" ")
#     print()


# # Pattern 6
# nums = 6
# while nums > 1:
#     for i in range(1,nums):
#         print(i,end =" ")
#     nums -= 1
#     print()


# # Pattern 7
# nums = 5
# for i in range(0,nums):
#     space = nums-i-1
#     star = (2*i)+1
#     print(" "*space, "*"*star)


# Pattern 8
# nums = 5
# for i in range(nums,0,-1):
#     star = (2*i)-1
#     space = nums-i
#     print(" "*space, "*"*star) 


# # Pattern 9
# nums = 5
# for i in range(0,nums):
#     space = nums-i-1
#     star = (2*i)+1
#     print(" "*space, "*"*star, " "*space)
# for i in range(nums,0,-1):
#     star = (2*i)-1
#     space = nums-i
#     print(" "*space, "*"*star, " "*space)


# Pattern 10
# nums = 1
# num = 5
# while nums < 6:
#     nums += 1
#     for i in range(0,nums-1):
#         print("*",end =" ")
#     print()
# while num > 1:
#     num -= 1
#     for i in range(0,num):
#         print("*",end =" ")
#     print()


## Pattern 11
# n = 5
# bit = 1
# for i in range(1, n + 1):
#     line = []
#     for j in range(i):
#         line.append(str(bit))
#         bit ^= 1           # flip 0<->1
#     print("".join(line))



# nums = [100,4,200,1,3,2]
# num = []
# count = 1
# new = list(sorted(set(nums))) #[1,2,3,4,100,200]
# for i in range(0,len(new)-1):
#     if new[i+1] - new[i] == 1:
#         count += 1
#     else:
#         num.append(count)
#         count = 1
# num.append(count)
# print(max(num))
# new = []
# curr_max = float('-inf')
# for i in range(-1,-len(nums)-1,-1):
#     if nums[i] > curr_max:
#         new.append(nums[i])
#         curr_max = nums[i]
# new.reverse()
# print(new)
# print(list(dict.fromkeys(nums)))

# def set_zeroes(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     # Step 1: find all positions where value is 0
#     zero_positions = []
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zero_positions.append((i, j))

#     # Step 2: set rows and columns to 0 for each zero position
#     for r, c in zero_positions:
#         # zero out the row r
#         for j in range(cols):
#             matrix[r][j] = 0

#         # zero out the column c
#         for i in range(rows):
#             matrix[i][c] = 0

#     return matrix


# # Example
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(set_zeroes(matrix))

nums = [1]
target = 1
l = 0
r = len(nums) - 1
while l <= r:
    middle = (l + r)//2
    if nums[middle] == target:
        if nums[middle - 1] == target:
            print([middle - 1, middle])
            break
        elif nums[middle + 1] == target:
            print([middle, middle + 1])
            break
        else:
            print([middle, middle])
            break

    elif nums[middle] < target:
        l = middle + 1

    else:
        r = middle - 1
print([-1, -1])