# WAF to print the sum of first n natural numbers using recursion.

def sum(num):
    if num == 0:
        return 0
    else:
        return num + sum(num - 1)
    
print(sum(5))


# WAF to print all elements of a list using recursion.

def elements(list, index = 0):
    if index == len(list):
        return
    else:
        print(list[index])
        elements(list, index + 1)

my_list = [1, 2, 3, 4, 5]
elements(my_list)