# Counting sort
def counting_sort(a_list):

    # find max element in list
    max_item = a_list[0]
    for item in a_list:
        if item > max_item:
            max_item = item

    # initialise the count_array
    count_array = [0] * (max_item + 1)
    print(count_array)

    # iterate through the input list again
    # put in the frequency into count_array
    for item in a_list:
        count_array[item] += 1
    print(count_array)

    # update and sort the list
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            a_list[index] = item
            index += 1

    # returns a sorted list
    return a_list



# Radix sort
def num_rad_sort(nums, b):
    # returns a sorted list nums in asc order
    return nums

# Driver code
nums = [43, 101, 22, 27, 5, 20, 15]
nums1 = [1,2,3,4,1,3,2,7]
print("nums1: " + str(nums1))
print(counting_sort(nums1))
print("Output: " + str(num_rad_sort(nums, 4)))