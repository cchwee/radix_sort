# Name: Cassandra Chwee (31544878)
# Title: FIT2004 Assignment 1 (Sem2, 2021)
# Description: A series of radix sort implementations.


# Task 1
# Counting sort
def counting_sort(a_list: list, base: int, exp: int) -> list:

    '''
    # Function: 
    This is an implementation of the non-comparison counting sort for a typical
    list of non-negative integers. The function is called by num_rad_sort
    recursively to sort of list of nums, a postive integer list.

    # Inputs: 
    a_list --> is a list which consists of only non-negative integers, 
    base --> is any integer value that is larger or equal to 2, 
    exp --> is an integer value of exponent. 

    # Output: 
    The output is a list which has been sorted. 

    # Time Complexity: 
    The complexity is O(N + U), where N is the size of the input array, whereas U 
    is a value which is dependent on the value of the given base.
    '''

    # initialise the count_array
    count_array = [[] for i in range(base+1)]

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

    '''
    # Function: 
    This is an implementation of the non-comparison radix sort for a typical
    list of non-negative integers. The function sorts from the LSB to MSB, by
    recursively calling the counting sort for every digit column.

    # Inputs: 
    nums --> is a list which consists of only non-negative integers, 
    b --> is any integer value that is larger or equal to 2.

    # Output: 
    The output is a list which has been sorted. 

    # Time Complexity: 
    The complexity is O(logbM * (N+b)), where b is the base, M would be the largest 
    value in nums, follwed by (N+b) which is contributed by the recursive calls of 
    counting sorts.
    '''
    
    # get the max num in nums
    if len(nums) > 0:
        max_num = nums[0]
        for item in nums:
            if item > max_num:
                max_num = item

        exp = 0
        while (max_num // b**exp) > 0:
            nums = counting_sort(nums, b, exp)
            exp += 1

    # returns a sorted list nums in asc order
    return nums



# Task 2
# Timing bases
import time
from typing import List

def base_timer(num_list: list, base_list: list) -> list:

    '''
    # Function: 
    This function acts as a timer for num_rad_sort for different bases, in order 
    for us to examine the runtime of it and understand how base values have effect
    on runtimes.

    # Inputs: 
    num_list --> is a list which consists of only non-negative integers, 
    base_list --> is a list of base with any integer value that is larger or equal 
    to 2, sorted in ascending order.

    # Output: The output is a list which has been sorted. 
    '''

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
# Driver code for Task 2 - done in google colab cuz my pc pip install suks 

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


# Task 3
# counting sort for string list
def countsort_strings(lst: list, col: int) -> list:

    '''
    # Function: 
    This is an implementation of the non-comparison counting sort for a list
    of strings. The function is called by radsort_strings recursively. 

    # Inputs: 
    lst --> is a list which consists of only strings, 
    col --> the column value of the strings

    # Output: 
    The output is a list of strings which has been sorted based on columns. 

    # Time Complexity: 
    The complexity is O(N + U), where N is the size of the input array, whereas U 
    is the number of buckets created in count_array.
    '''

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

    '''
    # Function: 
    This is an implementation of the non-comparison radix sort for a list 
    of strings. The function sorts the strings by their columns and calls
    countsort_strings recursively.

    # Inputs: 
    lst --> is a list which consists of only strings.

    # Output: 
    The output is a list of strings which has been sorted in lexicographic order. 

    # Time Complexity: 
    The complexity is O((N+U)*k), where k is dependent on the col values of the 
    longest string present in the list. (N+U) is contributed by the counting sorts.
    '''

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

    '''
    # Function: 
    This is an implementation of the non-comparison counting sort for a
    list of strings based on the length of the list.

    # Inputs: 
    lst --> is a list which consists of strings, 
    base --> is any integer value of base (in this case base 10 is used) 
    exp --> is an integer value of exponent

    # Output: 
    The output is a list of strings which has been sorted. 

    # Time Complexity: 
    The complexity is O(N + U), where N is the size of the input array, whereas U 
    is a value which is dependent on the value of the given base.
    '''

    # initialise the count_array
    count_array = [[] for i in range(base+1)]

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
def optimized_num_radsort(lst: list) -> list:

    '''
    # Function: 
    This is an implementation of the non-comparison radix sort for a
    list of strings based on the length of the list.

    # Inputs: 
    lst --> is a list which consists of only strings 

    # Output: 
    The output is a list of strings which has been sorted based on the total
    length of the list. 

    # Time Complexity: 
    The complexity is O((N+U)*k), where k is the digits in base 10, whereas
    (N+U) is contributed by the recursive calls of counting sorts.
    '''
    
    # checks for the need to sort
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

    '''
    # Function: 
    This is an simple implementation of comapring elements in
    two lists.

    # Inputs: 
    lst_a, lst_b --> a list which are to be compared

    # Output
    returns a boolean value True or False.

    # Time Complexity: 
    The complexity is O(n) if both lists have length n, and O(1) 
    if the lists have different lengths. Since there is a constraint of 
    comparing only same-length lists in the caller fucntion,
    the time complexity for this function is always O(1), constant time.
    '''

    # compare items in list a and list b
    for i in range(len(lst_a)):

        if lst_a[i] != lst_b[i]:
            return False

    return True


# perform in place swaps
def swap(lst, i, j):

    '''
    # Function: 
    This is an simple implementation of swapping elements in place.

    # Inputs: 
    lst --> a list where the swap is taking place at. 
    i --> index value
    j --> index value

    # Time Complexity: 
    The complexity is O(1), constant complexity.
    '''

    lst[i], lst[j] = lst[j], lst[i]


# place the same groups close to each another
def groups(lst):

    '''
    # Function: 
    This function groups the tuple list together based on the 
    same interests in the interest list.

    # Inputs: 
    lst --> a list of tuples which are to be grouped

    # Time Complexity: 
    The complexity is O(n) for worst case, where the algorithm 
    has to go through all n list items to find the same groups.
    '''

    pointer1 = 0
    pointer2 = 1

    while pointer1 < len(lst) and pointer2 < len(lst):

        list_a = lst[pointer1][1]
        list_b = lst[pointer2][1]

        # same length list --> compare
        if len(list_a) == len(list_b):

            # same interests groups
            if compare_lists(list_a, list_b):
                
                # swap to place them together
                swap(lst, pointer1+1, pointer2)
                pointer1 += 1
                pointer2 += 1

            # diff interest --> continue
            else:
                pointer2 += 1
                
        # diff length
        else:
            pointer1 += 1
            pointer2 = pointer1 + 1


# generate list of groups of people based on same interest
def group_ppl(lst):

    '''
    # Function: 
    This function generates the list of groups of people based
    on the same interests in the interest list.

    # Inputs: 
    lst --> a list of tuples which are to be grouped

    # Time Complexity: 
    The complexity is O(n), where the algorithm 
    has to go through all n list items to find the same groups.
    '''

    point_a = 0
    point_b = 1
    group_lst = []

    tmp = []
    tmp.append(lst[point_a][0])

    while point_a < len(lst) and point_b < len(lst):
        
        lsta = lst[point_a][1]
        lstb = lst[point_b][1]

        # if length is the same
        if len(lsta) == len(lstb):

            # same interests groups
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
        
        # different length of lists
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

    '''
    # Function: 
    This function generates the list of lists of people that have 
    identical interests.

    # Inputs: 
    data --> is a list, where each element is a 2-element tuple representing a person.
            First element is their name, and second is their interest list.

    # Time Complexity: 
    The complexity is O(NM), where N is the number of elements in data, and M is
    the max num of chars among all sets of interest.
    '''

    # if data is empty, return [], O(1)
    if len(data) == 0:
        return []

    # if data only has one person, return [person name], O(1)
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

