# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
#  a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1, n2):
    return sum(n1, n2) == 10



# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1, n2):
    if sum(n1, n2) == 10:
        return True
    else:
        return sum(n1, n2)



# ## Task 3
#
# Create a function that takes in a string and returns the
# first character of that string in upper case.

my_str = 'string'

def first_upper(my_String):
    # Given Solution
    return my_String[0].upper()
    
    # My Solution
    # temp = list(my_string)
    # for index, char in enumerate(temp):
    #     # print(f"char: {char} at index: {index}")
    #     if index == 0:
    #         temp[index] = char.upper()
    #         return temp[index]

print(first_upper(my_str))


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two characters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)

my_string = 'string'

def last_two(myString):
    if len(myString) < 2:
        return "Error"
    else:
        return myString[-2:]
        
print(last_two(my_string))

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

my_list = [4, 5, 1, 2, 3, 6, 7]

def seq_check(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

# ## Task 6
#
# Given 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**

def compare_len(s1, s2):
    if len(s1) > 0:
        return abs(len(s2) - len(s1))
    else:
        return 0

print(compare_len('string', 'string 2'))

# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
# value in that list.

my_list2 = [1, 2, 5, 7, 10, 18, 35, 84, 10, 22]

def sum_or_max(mylist):
    if len(mylist) % 2 == 0:
        print('Even, sum:')
        return sum(mylist)
    else:
        print('Odd, max:')
        return max(mylist)

print(sum_or_max(my_list2))