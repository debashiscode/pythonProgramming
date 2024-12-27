# some example of array in python
arr = [10, 20, 30]  # This array will store integer
arr2 = ['c', 'd', 'e']  # This array will store characters
arr3 = [28.5, 36.5]   # this array will store floating numbers
arr4 = [10,20,'1','b',11.4]  # is this an array ?

print(arr)
print(arr2)
print(arr3)
print(arr4)


arr = [5,6,7,8]  # this is a one dimensional array
print(arr[0])

# this is a two D array
two_d_array = [
    [5,6,7,8],
    [5,6,7,8]
]
print(two_d_array[0][1])

#this is an 3-d array
three_d_array = [
                   [
                       [4,5,6,7],
                       [6,7,8,9],
                   ],
                   [
                       [4,5,6,7],
                       [6,7,8,9],
                   ],
                ]
print(three_d_array[0][1][1])


#Example :  row major order answer  arr[0...5][0...10]

# No of column = upper bound - lower bound + 1 = 10-0+1 = 11
#  100 + 2 * ((3 - 0)*11 + (7-0))
# = 100 + 2*(33+7)
# = 100 + 80
# = 180
# arr[3][7] is 180


#Example :  column major order answer  arr[0...5][0...10]

# No of rows = upper bound - lower bound + 1 = 5-0+1 = 6
#  100 + 2 * ((7 - 0)*6 + (3-0))
# = 100 + 2*(42+3)
# = 100 + 90
# = 180
# arr[3][7] is 190


# Example 4
arr = [1, 2, 3, 4, 5]
print(arr[0], ", ", arr[4])

# Example 5
arr = [1, 2, 3, 4, 5]
print(arr[0], ", ", arr[-4])

# Example 6
arr = [1, 2, 3, 4, 5]
print(arr[-2], ", ", arr[3])


# Q1
"""
Which of the following points is/are true about Linked List data structure when it is compared with array?

(A) Arrays have better cache locality that can make them better in terms of performance.

(B) It is easy to insert and delete elements in Linked List

(C) Random access is not allowed in a typical implementation of Linked Lists

(D) The size of array has to be pre-decided, linked lists can change their size any time.

(E) All of the above
"""

#ans E








