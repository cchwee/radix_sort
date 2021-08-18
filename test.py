# # """
# # Test cases for FIT2004 2021 S2 Assignment 1 Task 1.

# # Assumes str_rad_sort (or whatever you call it) returns a new sorted copy
# # instead of sorting in place. Some minor modifications are required for
# # the test cases to work otherwise.
# # """

# # import unittest

# # # If your code is stored in other files,
# # # change the import path below
# # from assignment1 import *


# # # If your radix sort for strings function is not named
# # # str_rad_sort, uncomment the line below and set the
# # # r-value to the name of the function for it to work.
# # # This unifies the name of the radix sort function below.

# # str_rad_sort = radsort_strings


# # class TestStrRadixSort(unittest.TestCase):

# #     def test1(self):
# #         """ Edge case: List is empty.
# #         Author: Ci Leong
# #         """
# #         arr = []
# #         result = str_rad_sort(arr)
# #         self.assertEqual(result, [], msg=f'Cannot sort empty lists. Expected [], got {result}.')

# #     def test2(self):
# #         """ Tests whether strings are sorted lexicographically.
# #         Failure of this test could mean strings are sorted by numerical value.
# #         Or... it could be processed in other orders as well (might not even be ordered LOL).
# #         Author: Ci Leong
# #         """
# #         arr1 = ['ab', 'c']
# #         arr2 = ['c', 'ab']
# #         result1 = str_rad_sort(arr1)
# #         result2 = str_rad_sort(arr2)
# #         expected_result = ['ab', 'c']
# #         self.assertTrue(result1 == result2 == expected_result,
# #         msg=f'Strings are not sorted lexicographically or unsorted. Expected {expected_result}, got {result1} and {result2} (both must be correct)')

# #     def test3(self):
# #         """ Tests if ' ' and '' are wrongly placed in 'a''s bin.
# #         Failing this test case probably means there is no separated bins for '' and ' '.
# #         Author: Ci Leong
# #         """
# #         arr = [' ', '']
# #         result = str_rad_sort(arr)
# #         expected_result = ['', ' ']
# #         self.assertEqual(result, expected_result, msg=f'Expected {expected_result}, got {result}.')

# #         arr = ['a', '']
# #         result = str_rad_sort(arr)
# #         expected_result = ['', 'a']
# #         self.assertEqual(result, expected_result, msg=f'Expected {expected_result}, got {result}.')


# # class TestInterestGroups(unittest.TestCase):

# #     def setUp(self):
# #         pass

# #     def test1(self):
# #         pass
        

# # if __name__ == '__main__':
# #     unittest.main()

""" Test cases for Question 3 of FIT2004 Assignment """

__author__ = "Arthur Lee"

import unittest
from assignment1 import interest_groups


class TestInterestGroups(unittest.TestCase):
    def test1(self):
        """ Provided in Assignment Specifications """
        data = [("nuka", ["birds", "napping"]),
                ("hadley", ["napping birds", "nash equilibria"]),
                ("yaffe", ["rainy evenings", "the colour red", "birds"]),
                ("laurie", ["napping", "birds"]),
                ("kamalani", ["birds", "rainy evenings", "the colour red"])]

        expected = sorted([["laurie", "nuka"], ["hadley"], ["kamalani", "yaffe"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test2(self):
        """ Empty List """
        data = []

        expected = sorted([])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test3(self):
        """ All same single interest """
        data = [("john", ["coding"]),
                ("arthur", ["coding"]),
                ("jacky", ["coding"]),
                ("zach", ["coding"]),
                ("laura", ["coding"]),
                ("desmond", ["coding"]),
                ("benny", ["coding"]),
                ("casper", ["coding"])]

        expected = sorted([sorted(["john", "arthur", "jacky", "zach", "laura", "desmond", "benny", "casper"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test4(self):
        """ All same multiple interests sorted """
        data = [("timothy", ["jogging", "gaming", "fishing"]),
                ("jimmy", ["jogging", "gaming", "fishing"]),
                ("arthur", ["jogging", "gaming", "fishing"]),
                ("zim", ["jogging", "gaming", "fishing"]),
                ("lauren", ["jogging", "gaming", "fishing"]),
                ("yanny", ["jogging", "gaming", "fishing"]),
                ("benjamin", ["jogging", "gaming", "fishing"]),
                ("ethan", ["jogging", "gaming", "fishing"]),
                ("nate", ["jogging", "gaming", "fishing"])]

        expected = sorted([sorted(["timothy", "jimmy", "arthur", "zim", "lauren", "yanny", "benjamin", "ethan", "nate"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test5(self):
        """ All same multiple interests not sorted """
        data = [("timothy", ["jogging", "gaming", "fishing"]),
                ("jimmy", ["gaming", "jogging", "fishing"]),
                ("arthur", ["fishing", "gaming", "jogging"]),
                ("zim", ["jogging", "gaming", "fishing"]),
                ("lauren", ["jogging", "gaming", "fishing"]),
                ("yanny", ["jogging", "gaming", "fishing"]),
                ("benjamin", ["gaming", "fishing", "jogging"]),
                ("ethan", ["jogging", "fishing", "gaming"]),
                ("nate", ["fishing", "jogging", "gaming"])]

        expected = sorted([sorted(["timothy", "jimmy", "arthur", "zim", "lauren", "yanny", "benjamin", "ethan", "nate"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test6(self):
        """ All different single interest """
        data = [("jack", ["coding"]),
                ("nathan", ["teaching computer science"]),
                ("ian", ["educating students on algorithms and data structures"]),
                ("arthur", ["programming stuff"]),
                ("doris", ["chilling"]),
                ("timmy", ["feeding pigeons"]),
                ("aj", ["playing games"]),
                ("dawn", ["catching pokemon"]),
                ("light", ["killing people with a death note"])]

        expected = sorted([["jack"], ["nathan"], ["ian"], ["arthur"], ["doris"], ["timmy"], ["aj"], ["dawn"], ["light"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test7(self):
        """ All different multiple interests """
        data = [("arthur", ["coding", "playing video games", "math", "binging youtube"]),
                ("ash", ["becoming the greatest pokemon master of all time"]),
                ("ian", ["roasting other units", "teaching computer science"]),
                ("phoenix", ["legal assistance", "bluffing his way to victory"]),
                ("barbara", ["singing", "dancing", "becoming an idol"])]

        expected = sorted([["arthur"], ["ash"], ["ian"], ["phoenix"], ["barbara"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test8(self):
        """ If two different interest lists concatenate to the same string """
        data = [("arthur", ["car", "racing"]),
                ("jacky", ["carracing"])]

        expected = sorted([["arthur"], ["jacky"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test9(self):
        """ Only one person """
        data = [("arthur", ["coding", "math"])]

        expected = sorted([["arthur"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test10(self):
        """ Random example """
        data = [("tony", ["rich", "billionaire", "superhero"]),
                ("bruce", ["superhero", "rich", "billionaire"]),
                ("nolan", ["look at what they need to mimic a fraction of our power", "think mark think", "thats the neat part you dont"]),
                ("peter", ["superhero"]),
                ("steve", ["from another time", "superhero"])]

        expected = sorted([sorted(["tony", "bruce"]), ["steve"], ["nolan"], ["peter"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test11(self):
        """ Random example """
        data = [("jack", ["clash of clans", "clash royale"]),
                ("ian", ["apex legends", "dota two"]),
                ("arthur", ["genshin impact", "pokemon"]),
                ("desmond", ["pokemon", "genshin impact"]),
                ("nick", ["clash royale", "clash of clans"]),
                ("zachary", ["genshin impact", "honkai impact third", "apex legends"]),
                ("elaine", ["tears of themis", "ddlc"]),
                ("steve", ["cuphead", "undertale", "fortnite", "clash of clans"]),
                ("john", ["clash royale", "clash of clans"]),
                ("tim", ["genshin impact", "pokemon"]),
                ("dan", ["genshin impact", "pokemon"]),
                ("ronald", ["undertale", "cuphead", "clash of clans", "fortnite"]),
                ("daniel", ["pokemon", "genshin impact"])]

        expected = sorted([sorted(["jack", "nick", "john"]), ["ian"], sorted(["arthur", "desmond", "tim", "dan", "daniel"]), ["zachary"], ["elaine"], sorted(["steve", "ronald"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test12(self):
        """ There is one imposter among us """
        data = [("john", ["coding", "math"]),
                ("arthur", ["math", "coding"]),
                ("nick", ["math", "coding"]),
                ("ian", ["teaching computer science", "roasting other units"]),
                ("dave", ["math", "coding"])]

        expected = sorted([sorted(["john", "arthur", "nick", "dave"]), ["ian"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test13(self):
        """ All interests are pure spaces (Not sure if counts as empty string, but better to be safe than sorry) """
        data = [("arthur", ["   ", " "]),
                ("ethan", ["                       "]),
                ("dave", [" ", " ", " ", " ", " ", " "]),
                ("nathan", [" ", "      "]),
                ("apple", [" ", "   "]),
                ("ian", ["    "])]

        expected = sorted([sorted(["arthur", "apple"]), ["ethan"], ["dave"], ["nathan"], ["ian"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test14(self):
        """ Some interests are pure spaces (Better to be safe than sorry) """
        data = [("jimmy", ["   ", " "]),
                ("david", ["math", "                       ", "a    lie"]),
                ("nicki", [" "]),
                ("arthur", ["st u ff", "                                          ", " ", " ", " "]),
                ("ian", [" ", "   "]),
                ("apple", ["    "])]

        expected = sorted([sorted(["jimmy", "ian"]), ["david"], ["nicki"], ["arthur"], ["apple"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))


if __name__ == '__main__':
    unittest.main()
# """
# I mutated the original list so if you did not, please change it TQ 
# """
# from assignment1 import *
# import unittest

# class TestNumRadixSort(unittest.TestCase):

#     """
#     TASK 1
#     """
#     def test(self):
#         """
#         Description : Based on assignment specification and data
#         """
#         nums = [43, 101, 22, 27, 5, 50, 15]
#         your_input = num_rad_sort(nums, 10)
#         expected_result = [5, 15, 22, 27, 43, 50, 101]
#         self.assertEqual(your_input, expected_result, "The output does not equal to the inbuilt sort function value (TEST)")

#     def test1(self):
#         """
#         Description : Check for when list is empty
#         """
#         nums = []
#         your_input = num_rad_sort(nums, 10)
#         result = nums
#         self.assertEqual(your_input, [], "It did not pass the empty list check (TEST1)")
    
#     def test2(self):
#         """
#         Description : Check for when everything is of equal element
#         """
#         nums = [2,2,2,2,2,2,2]
#         expected_result = sorted(nums)
#         your_input = num_rad_sort(nums, 10)
#         result = nums
#         self.assertEqual(your_input, expected_result, "The output does not equal to the inbuilt sort function value (TEST2)")
    
#     def test3(self):
#         """
#         Description : Check if it's suitable to be use for bases from 2 - 1000
#         """
#         nums = [43, 101, 22, 27, 5, 50, 15]
#         expected_result = [5, 15, 22, 27, 43, 50, 101]
#         for base in range(2, 1000):
#             with self.subTest(base=base):
#                 your_input = num_rad_sort(nums, 10)
#                 result = nums
#                 self.assertEqual(your_input, expected_result, "The output does not equal to the inbuilt sort function value (TEST3)")

#     """
#     TASK 3 
#     """
#     def test4(self):
#         """
#         Description : Testing to check if interest group is working as expected
#         """
#         data = [("nuka", ["birds", "napping"]),
#         ("hadley", ["napping birds", "nash equilibria"]),
#         ("yaffe", ["rainy evenings", "the colour red", "birds"]),
#         ("kamalani", ["birds", "rainy evenings", "the colour red"]),
#         ("laurie", ["napping", "birds"])]
#         expected_result = [['laurie', 'nuka'], ['hadley'], ['kamalani', 'yaffe']]
#         self.assertEqual(interest_groups(data),expected_result, "The result for test 4 does not equal to the expected result (TEST4)")

#     def test5(self):
#         """
#         Description : Checking if radix_sort_string is working as intended
#         """
#         data = ["bcharacter","similar", "similar","as","ab","bchar","gabd","aa"]
#         expected_result = sorted(data)
#         your_input = radsort_strings(data)
#         self.assertEqual(your_input,expected_result, "The result for test 4 does not equal to the expected result (TEST4)")


# if __name__ == '__main__':
#     unittest.main()