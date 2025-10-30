# # program will start with a line "Welcome to Burger King"
# # user will be asked for a input this will be boolean True means veg false means non if true is given then ingridient will be potato otherwise chicken
# # user will be asked if bun should be gluten free 
# # user will be asked whether he wants red or white sauce
# # finally bunger object is created with correct ingridients 

# class Burger:
#     # patty = ""
#     # bun = ""
#     # sauce = ""
#     def __init__(self,patty,bun,sauce):
#         self.patty = patty
#         self.bun = bun
#         self.sauce = sauce
#         print(f"This Burger is made of ",self.patty.ingridient)
#         print("Sauce is ",self.sauce.type_of_sauce," sauce")
#         print("Buns made of ",self.bun.type_of_bun)

# class Patty:
#     # ingridient = "Potato"
#     c1 = Burger()
#     def __init__(self,veg_or_nonveg):
#         if veg_or_nonveg == "true":
#             self.ingridient = "Potato"
#         else:
#             self.ingridient = "Chicken"
    
#         # print("our patty is done.")

# class Sauce:
#     # type_of_sauce = "Red"
#     def __init__(self,redsauce_whitesauce):
#         if redsauce_whitesauce == "red":
#             self.type_of_sauce = "Red"
#         else:
#             self.type_of_sauce = "White"
        
#         # print("our patty is done.")

# class Bun:
#     # type_of_bun = "Wheat"
#     def __init__(self,typeofbun):
#         if typeofbun == "true":
#             self.type_of_bun = "Wheat"
#         else:
#             self.type_of_bun = "Flour"
        
#         # print("our patty is done.")


# print("<-----Welcome to Burger King----->")


# while True:
#     veg_or_nonveg = input("Do you want Veg Patty(true/false)").lower()
#     if veg_or_nonveg not in ["true","false"]:
#         print("Please Enter valid input")
#     else:
#         break
# while True:
#     redsauce_whitesauce = input("Do you want red sauce or white sauce ").lower()
#     if redsauce_whitesauce not in ["red","white"]:
#         print("Please Enter valid input")
#     else:
#         break
# while True:
#     typeofbun = input("Do you want Gluten Free bun (true/flase)").lower()
#     if typeofbun not in ["true","false"]:
#         print("Please Enter valid input")
#     else:
#         break

# pat = Patty(veg_or_nonveg)
# sau = Sauce(redsauce_whitesauce)
# bu = Bun(typeofbun)

# bug = Burger(pat,bu,sau)



class Solution(object):
    def findMin(self, nums):
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != 1:
                return nums[i]
            else:
                return nums[0]

s = Solution()
output = s.findMin([3,4,5,1,2])
print(output)