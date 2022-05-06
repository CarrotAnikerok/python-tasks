import numpy as np

#task 1

def up(number):
    a = np.zeros((number, number), dtype=np.int32)
    b = np.ones(number, dtype=np.int32)
    a[0] = b
    return a

print(up(10))

#task 2

def task_border(number):
    a = np.ones((number, number), dtype=np.int32)
    a[1:(number-1), 1:(number-1)] = 0
    return a

print(task_border(10))

#task 3

def task_2_5x5(number):
    a = np.ones((number, number), dtype=np.int32) + 1
    return a

print(task_2_5x5(5))

#task 4

def task_0123():
    a = np.zeros((10, 10), dtype=np.int32)
    a[0:5, 5:10] = 1
    a[5:10, 0:5] = 2
    a[5:10, 5:10] = 3
    return a

print(task_0123())

#task 5

#def task_chess():

#task 6

def task_1_to_9_lines():
    a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
    a = a.transpose()
    b = np.ones((9, 9), dtype=np.int32)
    return a*b

print(task_1_to_9_lines())
