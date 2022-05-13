import numpy as np


# task 1

def up(number):
    a = np.zeros((number, number), dtype=np.int32)
    b = np.ones(number, dtype=np.int32)
    a[0] = b
    return a


print("1 задание\n", up(10))


# task 2

def task_border(number):
    a = np.ones((number, number), dtype=np.int32)
    a[1:(number - 1), 1:(number - 1)] = 0
    return a


print("2 задание\n", task_border(10))


# task 3

def task_2_5x5(number):
    a = np.ones((number, number), dtype=np.int32) + 1
    return a


print("3 задание\n", task_2_5x5(5))


# task 4

def task_0123():
    a = np.zeros((10, 10), dtype=np.int32)
    a[0:5, 5:10] = 1
    a[5:10, 0:5] = 2
    a[5:10, 5:10] = 3
    return a


print("4 задание\n", task_0123())


# task 5

def task_chess():
    matrix1 = np.ones((10), dtype=np.int32)
    matrix1[0:9:2] = matrix1[0:9:2] * 0
    matrix2 = np.zeros((10), dtype=np.int32)
    matrix2[0:9:2] = matrix2[0:9:2] + 1
    matrix3 = np.ones((10, 10), dtype=np.int32)
    matrix = matrix2 * matrix3
    matrix[0:9:2] = matrix1

    return matrix


print("5 задание, шахматы\n", task_chess())


# task 6

def task_1_to_9_lines():
    a = np.arange(1, 10)
    a = a.transpose()
    b = np.ones((9, 9), dtype=np.int32)
    return a * b


print("6 задание\n", task_1_to_9_lines())


# task 7
def task_1_to_100():
    matrix1 = np.arange(1, 11)
    matrix2 = np.ones((10, 10), dtype=np.int32)
    matrix1 = matrix1 * matrix2
    a = 10
    for i in range(1, 10):
        matrix1[i, :] = matrix1[i, :] + a
        a += 10
    return matrix1


print("7 задание\n", task_1_to_100())


