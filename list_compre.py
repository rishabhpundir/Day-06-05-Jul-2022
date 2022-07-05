# Given a list of numbers, remove all odd numbers from the list:

# numbers = [3,5,45,97,32,22,10,19,39,43]
# result = [num for num in numbers if num%2 == 0]
# print(result)


# -------------------------------------------------------------------------------------------------------------------------


# Find all of the numbers from 1-1000 that are divisible by 7

# list_1_to_1000 = [num for num in range(1, 1000) if num%7 == 0]
# print(list_1_to_1000)


# -------------------------------------------------------------------------------------------------------------------------


# Find all of the numbers from 1-1000 that have a 3 in them

# list_of_no_with_3_in_them = [num for num in range(0, 1000) if '3' in str(num)]
# print(list_of_no_with_3_in_them)


# -------------------------------------------------------------------------------------------------------------------------


# Count the number of spaces in a string

# sentence = str(input('Enter a sentence : '))
# chars_in_sentence = [word for word in sentence if sentence.split()]
# space = ' '
# i=0
# for item in chars_in_sentence:
#     if item == space:
#         i+=1

# print(f'No. of spaces in sentence are : {i}')


# -------------------------------------------------------------------------------------------------------------------------


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

# string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
# consonants = [char for char in string if char not in 'aeiou ']
# print(consonants)


# -------------------------------------------------------------------------------------------------------------------------


# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# common_no = [num for num in list_a if num in list_b]
# print(common_no)


# -------------------------------------------------------------------------------------------------------------------------


# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’

# string = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# split_words = string.split()
# numbers = [int(num) for num in split_words if not num.isalpha()]

# print(numbers)


# -------------------------------------------------------------------------------------------------------------------------


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

# odd_or_even = ['odd' if num%2 != 0 else 'even' for num in range(20)]
# print(odd_or_even)


# -------------------------------------------------------------------------------------------------------------------------


# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_b = [2, 7, 1, 12]

# matching_no = [(num, num) for num in list_a if num in list_b]
# print(matching_no)


# -------------------------------------------------------------------------------------------------------------------------


# Find all of the words in a string that are less than 4 letters

# string = str(input("Enter a sentence : "))
# split_words = string.split()
# less_than_4_words = [word for word in split_words if len(word) < 4]
# print(less_than_4_words)


# -------------------------------------------------------------------------------------------------------------------------


# Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)

# numbers_list= [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
# print(numbers_list)


# -------------------------------------------------------------------------------------------------------------------------



