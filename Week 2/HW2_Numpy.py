import numpy as np

a = np.array([3,2,1,7,4,8])
b = np.array([4,5,6,2,8])

# 1. Vertical Stack
#print(np.vstack((a,b)))

# Horizontal Stack 
# print(np.hstack((a,b)))

# 2. Common elements
# print(np.intersect1d(a,b))

# 3. Exract elements within range
# print(np.where((a >=5) & (a<11)))

# 4. Iris
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter =',', dtype='float', usecols=[0,1,2,3])

# elem_count = 0
# new_arr = []
# for elem in iris_2d:    
#     if (iris_2d[elem_count:elem_count+1,:2] > 1.5) & ((iris_2d[elem_count:elem_count+1,0]) < 5.0):
#         x = iris_2d[elem_count:elem_count+1,:]
#         new_arr = np.concatenate([x,])
#     elem_count += 1
#     print(new_arr)


condition = np.logical_and(iris_2d[:, 2] > 1.5, iris_2d[:, 0] < 5.0)
# Select the rows where the condition is True
x = iris_2d[condition, 2]
y = iris_2d[condition, 0]

# Concatenate the filtered columns into a new array
new_arr = np.column_stack((x, y))
print(new_arr)