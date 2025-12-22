#Первый файл "sorting_module.py"
"Модуль"
def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        for j in range(i, 0, -1):
            if (result[j] < result[j-1]):
                result[j], result[j-1] = result[j-1], result[j]
    return result

def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def selection_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result

#Второй файл "main.py"
import sorting_module

if __name__ == "__main__":
    print("Используем модуль")

    numbers = [7, 3, 9, 2, 5]
    print('Изначальный массив:')
    print(numbers)
    print()

    print("Сортировка методом вставки:")
    print(sorting_module.insertion_sort(numbers))
    print()

    print("Сортировка методом обмена:")
    print(sorting_module.bubble_sort(numbers))
    print()

    print("Сортировка методом выбора:")
    print(sorting_module.selection_sort(numbers))
    print()
