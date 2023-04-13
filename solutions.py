"""
1. Write a Python Program to find sum of array?
"""
array = [10, 20, 30, 40, 50]

sum = 0

for i in array:
   sum += i

print("The sum of the array is:", sum)

"---------------------------------------------------------------------------------------------"

"""
2. Write a Python Program to find largest element in an array?
"""
array = [10, 20, 30, 40, 50]

max_num = array[0]

for i in array:
   if i > max_num:
      max_num = i

print("The largest element in the array is:", max_num)

"---------------------------------------------------------------------------------------------"

"""
3. Write a Python Program for array rotation?
"""
def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    arr = arr[d:] + arr[:d]
    return arr

array = [10, 20, 30, 40, 50]
rotation = 2

rotated_array = rotate_array(array, rotation)

print("Original array:", array)
print("Rotated array:", rotated_array)

"---------------------------------------------------------------------------------------------"

"""
4. Write a Python Program to Split the array and add the first part to the end?
"""
def split_array(arr, n, k):
   for i in range(0, k):
      x = arr[0]
      for j in range(0, n-1):
         arr[j] = arr[j+1]
      arr[n-1] = x
   return arr

array = [10, 20, 30, 40, 50]
k = 2

split_array = split_array(array, len(array), k)

print("Original array:", array)
print("Split and rotated array:", split_array)

"---------------------------------------------------------------------------------------------"

"""
5. Write a Python Program to check if given array is Monotonic?
"""
def is_monotonic(arr):
   return (all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or
           all(arr[i] >= arr[i+1] for i in range(len(arr)-1)))

array = [10, 20, 30, 40, 50]

if is_monotonic(array):
   print("The array is monotonic")
else:
   print("The array is not monotonic")

   "---------------------------------------------------------------------------------------------"

