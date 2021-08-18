# Task 1
# Counting sort
def counting_sort(a_list: list, base: int, exp: int) -> list:

    # initialise the count_array
    count_array = [[] for i in range(base+1)]
    # print("empty count arr: " + str(count_array))

    # put in the item as linked list into count_array
    for num in a_list:
        digit = (num // base ** exp) % base 
        count_array[digit].append(num)

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
def countsort_strings(lst: list, col: int) -> list:

    # initialise the count_array
    # bucket for "no-need to sort", '', ' ', a-z
    count_array = [[] for i in range(29)]

    # four scenarios: need to sort('', ' ', a-z), no need to sort
    for interest in lst:
        
        # special case for empty string
        if interest == '':
            count_array[1].append(interest)

        # short strings --> no need to sort
        elif len(interest) -1 < col and interest != '':
            count_array[0].append(interest)
        
        # has column, need to sort
        else:
            
            # if col is a space --> put in ' ' bucket
            if interest[col] == ' ':
                count_array[2].append(interest)
            
            # if col is a-z char, sort as normal
            else:
                val = ord(interest[col]) - ord('a') + 3
                count_array[val].append(interest)

    # return output sorted list based on col
    output_lst = []
    
    for sorted_lst in count_array:
        for interest in sorted_lst:
            output_lst.append(interest)

    return output_lst


# radix sort from msb char --> lsb char
def radsort_strings(lst: list) -> list:

    # get the max length in lst of strings
    if len(lst) > 1:
        max_len = len(lst[0])
        for i in range(len(lst)):
            len_str = len(lst[i])
            if len_str > max_len:
                max_len = len_str

        # perform sort from LSB col --> MSB col
        for col in range((max_len-1), -1, -1):
            lst = countsort_strings(lst, col)

    return lst        


# optimized count sort to sort based on length to place close tgt
def optimized_countsort(lst, base, exp):

    # initialise the count_array
    count_array = [[] for i in range(base+1)]

    # formula = (number // base**exp) % base 
    # put in the item as linked list into count_array
    for item in lst:
        digit = (len(item[1]) // base ** exp) % base 
        count_array[digit].append(item)
    # print("now: " + str(count_array))

    # iterate through count_array and return output
    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    # returns a sorted list
    return output_lst


# optimized num rad sort to sort based on length
def optimized_num_radsort(lst):

    if len(lst) > 1:
        # get max length 
        max_len = len(lst[0][1])
        for item in lst:
            interest_lst = item[1]
            if len(interest_lst) > max_len:
                max_len = len(interest_lst)

        exp = 0
        while (max_len // 10**exp) > 0:
            lst = optimized_countsort(lst, 10, exp)
            exp += 1

    # return output of sorted lst
    return lst


# compare two equal length lists, returns a Boolean
def compare_lists(lst_a: list, lst_b: list) -> bool:

    # compare items in list a and list b
    for i in range(len(lst_a)):
        if lst_a[i] != lst_b[i]:
            return False
    return True


# check for groups in lists of list
def check_groups(lst):

    # check for groups
    group_lst = []
    pointer_1 = 0
    pointer_2 = 1

    # pointer_1 first item, append name to group
    tmp_lst = []
    tmp_lst.append(lst[pointer_1][0])

    # while loop to loop through data items
    while pointer_1 < len(lst) and pointer_2 < len(lst):

        # go through data items
        list_a = lst[pointer_1][1]
        list_b = lst[pointer_2][1]

        # if same length --> do comparison
        if len(list_a) == len(list_b):

            # if same group, append pointer_2 to tmp_lst
            if compare_lists(list_a, list_b):
                tmp_lst.append(lst[pointer_2][0])

                # pop the person with same interest
                lst.pop(pointer_2)
            
            # if false, continue to scan through
            else:
                pointer_2 += 1
        
        # else, definitely not in same group (diff length)
        else:

            # append the current group to group list
            group_lst.append(tmp_lst)

            # remove the current person 
            lst.pop(pointer_1)
        
            # reset the pointers
            pointer_1 = 0
            pointer_2 = 1

            # reset tmp_lst
            tmp_lst = []
            tmp_lst.append(lst[pointer_1][0])
    
    # remaining in tmp_lst belongs to previous group
    group_lst.append(tmp_lst)
    lst.pop(pointer_1)

    # remaining list append to new group
    while len(lst) != 0:
        group_lst.append([lst[0][0]])
        lst.pop(0)

    return group_lst


# interest group function
def interest_groups(data) -> list:

    # if data is empty, return []
    if len(data) == 0:
        return []

    # if data only has one person, return [person name]
    elif len(data) == 1:
        return [[data[0][0]]]
    
    # if data has 2 persons or more
    else:
        
         # do radix sort on interest list in each tuple
        temp_lst = []

        for tuple_pair in data:
            interest_lst = tuple_pair[1]
            sorted_lst = radsort_strings(interest_lst)
            temp_lst.append([tuple_pair[0], sorted_lst])

        # sort based on length of interest list to arrange closer
        data_copied = optimized_num_radsort(temp_lst)

        # check for groups
        groups_data = check_groups(data_copied)

        # sort name in list 
        sorted_name = []
        for name_lst in groups_data:
            name_lst_sort = radsort_strings(name_lst)
            sorted_name.append(name_lst_sort) 

        # return list of list with people of same interests
        return sorted_name


