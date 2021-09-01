# Counting sort
def counting_sort(a_list: list, base: int, exp: int) -> list:

    count_array = [[] for i in range(base+1)]

    # put in the item as linked list into count_array
    for num in a_list:
        digit = (num // base ** exp) % base 
        count_array[digit].append(num)

    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    return output_lst


# Radix sort
def num_rad_sort(nums: list, b: int) -> list:

    if len(nums) > 0:
        max_num = nums[0]
        for item in nums:
            if item > max_num:
                max_num = item

        exp = 0
        while (max_num // b**exp) > 0:
            nums = counting_sort(nums, b, exp)
            exp += 1

    return nums



# Timing bases
import time
from typing import List

def base_timer(num_list: list, base_list: list) -> list:

    output_lst = []

    for b in base_list:

        start_time = time.time()
        num_rad_sort(num_list, b)
        end_time = time.time()
        duration = end_time - start_time

        output_lst.append(duration)

    return output_lst


'''
# Driver code
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

fig1 = plt.figure()
plt.plot(bases1, y1, label = "line y1")
plt.plot(bases1, y2, label = "line y2")
plt.xscale('log')
plt.xlabel('log(bases1)')
plt.ylabel('Runtime')
plt.title('Graph of y1 and y2 vs log(bases1)')
plt.legend()
plt.show()

fig2 = plt.figure()
plt.plot(bases2, y3, label = "line y3")
plt.plot(bases2, y4, label = "line y4")
plt.xlabel('bases2')
plt.ylabel('bases2')
plt.title('Graph of y3 and y4 vs bases2')
plt.legend()
plt.show()

'''

# counting sort for string list
def countsort_strings(lst: list, col: int) -> list:

    # buckets for "no-need to sort", '', ' ', a-z
    count_array = [[] for i in range(29)]

    for interest in lst:
        
        if interest == '':
            count_array[1].append(interest)
        elif len(interest) -1 < col and interest != '':
            count_array[0].append(interest)
        else:
            
            if interest[col] == ' ':
                count_array[2].append(interest)
            else:
                val = ord(interest[col]) - ord('a') + 3
                count_array[val].append(interest)

    output_lst = []
    for sorted_lst in count_array:
        for interest in sorted_lst:
            output_lst.append(interest)

    return output_lst


# radix sort from msb char --> lsb char
def radsort_strings(lst: list) -> list:

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

    count_array = [[] for i in range(base+1)]

    # put in the item as linked list into count_array
    for item in lst:
        digit = (len(item[1]) // base ** exp) % base 
        count_array[digit].append(item)

    output_lst = []
    for lst in count_array:
        for item in lst:
            output_lst.append(item)

    return output_lst


# optimized num rad sort to sort based on length
def optimized_num_radsort(lst: list) -> list:

    if len(lst) > 1:
        max_len = len(lst[0][1])

        for item in lst:
            interest_lst = item[1]
            if len(interest_lst) > max_len:
                max_len = len(interest_lst)

        exp = 0
        while (max_len // 10**exp) > 0:
            lst = optimized_countsort(lst, 10, exp)
            exp += 1

    return lst


# compare two equal length lists, returns a Boolean
def compare_lists(lst_a: list, lst_b: list) -> bool:
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

        if len(list_a) == len(list_b):

            if compare_lists(list_a, list_b):
        
                swap(lst, pointer1+1, pointer2)
                pointer1 += 1
                pointer2 += 1

            else:
                pointer2 += 1
                
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

        if len(lsta) == len(lstb):

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

    if len(data) == 0:
        return []

    elif len(data) == 1:
        return [[data[0][0]]]

    else:

        temp_lst = []

        for tuple_pair in data:
            interest_lst = tuple_pair[1]
            sorted_lst = radsort_strings(interest_lst)
            temp_lst.append([tuple_pair[0], sorted_lst])

        data_copied = optimized_num_radsort(temp_lst)
        groups(data_copied)

        groups_data = group_ppl(data_copied)

        sorted_name = []
        for name_lst in groups_data:
            name_lst_sort = radsort_strings(name_lst)
            sorted_name.append(name_lst_sort) 

        return sorted_name

