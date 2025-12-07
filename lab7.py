import time
import random

# --- 1. АЛГОРИТМИ СОРТУВАННЯ ---

def bubble_sort(arr):
    n = len(arr)
    a = arr[:] 
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    n = len(arr)
    a = arr[:]
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# --- 2. ПОШУК МАКСИМУМУ ---

def find_max_ops(arr):
    ops = 0
    if not arr:
        return None, ops
    
    max_val = arr[0]; ops += 1 
    
    for i in range(1, len(arr)):
        ops += 1
        ops += 1 
        if arr[i] > max_val:
            max_val = arr[i]; ops += 1 
            
    return max_val, ops

def find_max_time(arr):
    start = time.perf_counter()
    max_val = max(arr)
    end = time.perf_counter()
    return max_val, (end - start) * 1000 

# --- 3. ЛІНІЙНИЙ ПОШУК ---

def linear_search(arr, key):
    start = time.perf_counter()
    for i in range(len(arr)):
        if arr[i] == key:
            end = time.perf_counter()
            return i, (end - start) * 1000
    end = time.perf_counter()
    return -1, (end - start) * 1000

# --- 4. МАТРИЦІ ---

def generate_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def matrix_add(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    
    start = time.perf_counter()
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    end = time.perf_counter()
    return C, (end - start) * 1000

def matrix_mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        return None, 0
        
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    start = time.perf_counter()
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    end = time.perf_counter()
    return C, (end - start) * 1000

if __name__ == "__main__":
    # Дані для сортування
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nВхідний масив: {test_arr}")
    print(f"Bubble Sort: {bubble_sort(test_arr)}")
    print(f"Quick Sort: {quick_sort(test_arr)}")
    
    # Тест пошуку максимуму
    max_val, ops = find_max_ops(test_arr)
    print(f"\nПошук максимуму (значення): {max_val}, Операцій: {ops}")
    
    # Тест лінійного пошуку
    idx, t = linear_search(test_arr, 22)
    print(f"Лінійний пошук (число 22): індекс {idx}, час {t:.5f} мс")
    
    # Матриці
    print("\n--- Матриці ---")
    m1 = generate_matrix(50, 50)
    m2 = generate_matrix(50, 50)
    
    _, t_add = matrix_add(m1, m2)
    print(f"Додавання матриць 50x50: {t_add:.5f} мс")
    
    _, t_mult = matrix_mult(m1, m2)
    print(f"Множення матриць 50x50: {t_mult:.5f} мс")