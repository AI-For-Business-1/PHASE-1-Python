
import numpy as np

# list= [3,5,3]
# array = np.array(list)
# print (array)
# print(list)
# print (type(array)) # numpy.ndarray
# print (type(list)) # list

# a=np.array(1) # zero-dimensional array
# b=np.array([1,3]) # one-dimensional array
# c=np.array([[1,3],
#             [5,6]]) # two-dimensional array

# # three-dimensional array
# d=np.array([[[3,5],[3 ,4]],#index 0
#             [[4,4],[3,3]]]) #index1

# comparing the dimensions of the arrays
# print(a.ndim) # 0
# print("@"*20) # 1
# print(b.ndim) # 1 
# print("@"*20) # 1
# print(c.ndim) # 2
# print("@"*20) # 1
# print(d.ndim) # 3
# print("@"*20) # 1

# # print arrays
# print(a) # ()
# print("*"*20) # 1

# print(b) # [1 3]
# print("*"*20) # 1

# print(c) # [[1 3]
#          #  [5 6]]
# print("*"*20) # 1

# print(d) # [[[3  5]
#          #   [ 3 4]]
#          #  [[ 4 4]
#          #   [3  3]]]

# print ("*"*20) # 1
# #indexing the three-dimensional array
# # in
# print (d[1,1,1])
# # indexing last element of the three-dimensional array by Negative indexing
# print (d[-1,-1,-1]) # 3
# #my custom array
my_array = np.array([1,2,3],ndmin=3) # three-dimensional array 
# [1,2,3],
#  [1,2,3],
#  [1,2,3]

print(my_array)
print (my_array[0]) # 1
print (my_array[0,0]) # 1
print (my_array[0,0,0]) # 1
print (my_array[-1,-1,-1]) # 3

# Lack of quantified achievements (medium)
# ATS and recruiters favor resumes with measurable impact to demonstrate effectiveness and results.
# Fix: Add metrics such as performance improvements, number of users impacted, or efficiency gains in projects and internships.
# Inconsistent date formatting (low)
# Inconsistent date formats can confuse ATS parsing and reduce readability.
# Fix: Standardize date formats throughout the resume, e.g., 'Month Year – Month Year'.
# Contact info lacks clickable links (low)
# Clickable LinkedIn, GitHub, and portfolio links improve recruiter engagement and ATS parsing.
# Fix: Add full URLs or hyperlink text for LinkedIn, GitHub, and portfolio.

