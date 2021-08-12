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

# Driver code
nums = [43, 101, 22, 27, 5, 50, 15]
nums1 = [1,2,3,1,3,2,4]
print("nums: " + str(nums))
print(num_rad_sort(nums, 4))
print("nums1: " + str(nums1))
print(num_rad_sort(nums1, 4))