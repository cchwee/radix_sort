# Task 1
# Counting sort
def counting_sort(a_list: list, base: int, exp: int) -> list:

    # initialise the count_array
    count_array = [[] for i in range(base+1)]
    # print("empty count arr: " + str(count_array))

    # formula = (number // base**exp) % base 
    # put in the item as linked list into count_array
    for num in a_list:
        digit = (num // base ** exp) % base 
        count_array[digit].append(num)
    # print("now: " + str(count_array))

    # iterate through count_array and return output
    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    # returns a sorted list
    return output_lst


# Radix sort
def num_rad_sort(nums: list, b: int) -> list:
    
    # get the max num in nums
    if len(nums) > 0:
        max_num = nums[0]
        for item in nums:
            if item > max_num:
                max_num = item
        # print("max num is: " + str(max_num))

        exp = 0
        while (max_num // b**exp) > 0:
            nums = counting_sort(nums, b, exp)
            exp += 1
            # print(nums)

    # returns a sorted list nums in asc order
    return nums



# Task 2
# Timing bases
import time

def base_timer(num_list: list, base_list: list) -> list:

    # an empty list to store the time taken
    output_lst = []

    # iterate through bases in base_list
    for b in base_list:

        # time the time taken for rad_sort
        start_time = time.time()
        num_rad_sort(num_list, b)
        end_time = time.time()
        duration = end_time - start_time

        # append time to output list
        output_lst.append(duration)
    
    # returns a list of numbers (time)
    return output_lst


'''
# Driver code for Task 2
# creates 4 lists of data to test base_timer
import random

random.seed("FIT2004S22021")
data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]
y1 = base_timer(data1, bases1)
y2 = base_timer(data2, bases1)
y3 = base_timer(data1, bases2)
y4 = base_timer(data2, bases2)
print(bases1)
print(bases2)
print(y1)
print(y2)
print(y3)
print(y4)
'''


# Task 3
# counting sort for string list
def countsort_strings(lst: list, col: int, base: int, min_base: int) -> list:

    # initialise the count_array
    count_array = [[] for i in range(base-1)]

    # sort according to char[col]
    for interest in lst:
        if len(interest)-1 < col or interest[col] == " ":
            count_array[0].append(interest)
        else:
            val = ord(interest[col]) - min_base
            count_array[val].append(interest)

    # return output sorted list based on col
    output_lst = []
    for sorted_lst in count_array:
        for interest in sorted_lst:
            output_lst.append(interest)

    return output_lst


# radix sort from msb char --> lsb char
def radsort_strings(lst: list, base: int, min_base: int) -> list:

    # get the max length in lst of strings
    if len(lst) > 1:
        max_len = len(lst[0])
        for i in range(len(lst)):
            len_str = len(lst[i])
            if len_str > max_len:
                max_len = len_str

        # perform sort from LSB col --> MSB col
        for col in range((max_len-1), -1, -1):
            result_lst = countsort_strings(lst, col, base, min_base)

    return result_lst        


# compare two equal length lists, returns a Boolean
def compare_lists(lst_a: list, lst_b: list) -> bool:

    # compare items in list a and list b
    for item_a in lst_a:
        for item_b in lst_b:
            if item_a != item_b:
                return False
    return True


def interest_groups(data) -> list:

    # intialise base values
    base = 26
    min_base = ord('a')

    # do radix sort on interest list in each tuple
    temp_lst = []
    
    for tuple_pair in data:
        interest_lst = tuple_pair[1]
        sorted_lst = radsort_strings(interest_lst, base, min_base)
        temp_lst.append((tuple_pair[0], sorted_lst))

    print(temp_lst)    
    # sort based on length of interest list - counting sort in T1
    

    # compare item of same length

    return


# Driver code for Task 3
data = [("nuka", ["birds", "napping"]),("hadley", ["napping birds", "nash equilibria"]),("yaffe", ["rainy evenings", "the colour red", "birds"]),("laurie", ["napping", "birds"]),("kamalani", ["birds", "rainy evenings", "the colour red"])]
print(interest_groups(data))
# print(data[1][0])

