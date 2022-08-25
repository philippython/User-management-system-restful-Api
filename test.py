from array import array
# from cgi import print_directory
# from collections import UserList
# # bytes
# # range of 0, 256
# data = [1, 2,3,4,5]
# list_2 = [6, 7,9]
# list_3 = list()
# tuple = (1, 2, 3, 4,5)

# test_set = {"mihai", "philip"}
# # print(dir(test_set))

print(dir(set))

# l1 = [1, 2, 3, 'a']
# reversed_l1 = l1[::-1]
# [start:stop:steps]
# print(reversed_l1) 
#  'a' 3 2 1
# l2 = l1
# l1.append(5)
# print(l2, l1)
# print(id(l2), id(l1))
# def mybill(bill):
#     print("Your bill is $ %s" % bill)
#     print(f"Your bill is ${bill}")

# print(dir(array))
# mybill(20)
# # list, bytearray, dict, 
# # list.append(6)
# # list.extend(list_2)
# # print(list)

# class House:
#     def __init__(self, color):
#         self.color = color

   

# class Luxoft(House):
#     def __init__(self, color, windows):
#         super().__init__(color)
#         self.windows = windows

#     @classmethod
#     def num_of_windows(cls, windows):
#         return cls(windows)

#     @staticmethod

#     def structure(self):
#         print(f"A building with {self.windows} windows")


# luxoft = Luxoft("purple", 100)
# luxoft.structure()


# Write an initializer which takes color as an argument and puts it inside the new object as an instance variable
# Write a subclass which inherits from house, adds the number of windows in its initializer but also makes use of the parent to initialize the color.


    
# lambda paremeters : x + y + z

# addition = lambda x, y, z : x + y + z

# print(addition(2, 3,4))

# employees = ["philip", "odulaja", "mary", "jones"]
# title_case = [name.title() for name in employees]
# print(title_case)

# even_numbers_less = [num for num in range(0, 101) if num % 2 == 0]
# print(even_numbers_less)

def add_to_list(item, lst=[]):
    lst.append(item)
    print(lst)
my_list = [1, 2, 3]
add_to_list(4) 
# [4]
add_to_list(5, my_list)
#  [1, 2, 3, 5]
add_to_list(6) 
# [4, 6]
add_to_list(7, my_list)
#  [1, 2, 3, 5, 7]
add_to_list(8)
# [4, 6, 8]

# print(dir(__builtins__))

# # object relational mapp

