# Radix Sort

## Background Info: Task 1 - Integer Radix Sort
You need to use radix sort to sort a given list of integers into ascending numerical order, using a given base.

## Input
**nums** is a unsorted list of non-negative integers

**b** is an integer, with value ≥ 2

## Output
**num_rad_sort** returns a list of integers. This list will contain exactly the same elements as **nums**, but sorted into ascending numerical order.

## Example
```
nums = [43, 101, 22, 27, 5, 50, 15]
>>>num_rad_sort(nums, 4)
[5, 15, 22, 27, 43, 50, 101]
```

## Complexity
**num_rad_sort** should run in O((n + b) ∗ logbM) time where:
- n is the length of nums
- b is the value of b
- M is the numerical value of the maximum element of nums

<br />

## Background Info: Task 2 - Timing Bases
Write a function ```base_timer(num_list, base_list)``` which you will use to investigate the relationship between the base used and the runtime.

Uncomment the code in the ```assignment.py``` to create four lists of data and produce output for them.

## Input
**num_list** is a list of non-negative integers.

**base_list** is a list of integers, all with values ≥ 2, sorted ascending.

## Output
**base_timer** returns a list of numbers. Element i in this list is the time taken to run your radix sort from Task 1 on num_list using element i from base_list as the base.


<br />

## Background Info: Task 3 - Interest Groups




