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


# perform in place swaps
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


# place the same groups close to each another
def groups(lst):

    pointer1 = 0
    pointer2 = 1

    while pointer1 < len(lst) and pointer2 < len(lst):

        list_a = lst[pointer1][1]
        list_b = lst[pointer2][1]

        # same length
        if len(list_a) == len(list_b):

            # same
            if compare_lists(list_a, list_b):
                
                # swap
                swap(lst, pointer1+1, pointer2)
                pointer1 += 1
                pointer2 += 1

            # not same
            else:
                pointer2 += 1
                
        # diff length
        else:
            pointer1 += 1
            pointer2 = pointer1 + 1


# generate list of groups of people based on same interest
def group_ppl(lst):
    point_a = 0
    point_b = 1
    group_lst = []

    tmp = []
    tmp.append(lst[point_a][0])

    while point_a < len(lst) and point_b < len(lst):
        
        lsta = lst[point_a][1]
        lstb = lst[point_b][1]

        if compare_lists(lsta, lstb):
            tmp.append(lst[point_b][0])
            point_b += 1

        else:
            group_lst.append(tmp)

            # reset tmp
            point_a = point_b
            point_b = point_a + 1
            tmp = []
            tmp.append(lst[point_a][0])
    
    group_lst.append(tmp)

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
        
        # make groups next to each other
        groups(data_copied)

        # generating list of names based on same group 
        groups_data = group_ppl(data_copied)

        # sort name in list 
        sorted_name = []
        for name_lst in groups_data:
            name_lst_sort = radsort_strings(name_lst)
            sorted_name.append(name_lst_sort) 

        # return list of list with people of same interests
        return sorted_name

