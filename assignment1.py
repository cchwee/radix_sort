# Task 1
# Counting sort
def counting_sort(a_list, base, exp):

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
def num_rad_sort(nums, b):
    
    # get the max num in nums
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


import time

# Task 2
# Timing bases
def base_timer(num_list, base_list):

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
# Driver code for Task 1
nums = [43, 101, 22, 27, 5, 50, 15]
nums1 = [1,2,3,1,3,2,4]
print("nums: " + str(nums))
print(num_rad_sort(nums, 4))
print("nums1: " + str(nums1))
print(num_rad_sort(nums1, 4))
'''

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

import pandas

# Task 3
def interest_groups(data):
    pass

