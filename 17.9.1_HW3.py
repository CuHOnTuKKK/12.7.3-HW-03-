fail = 'необходимо перезапустить программу'
numbers_order = input('Введите целые числа через пробел: ')
entered_number = int(input('Введите любое целое число: '))


# Функция для определения цифр в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


# Проверка соответствия указанному в условии ввода данных.

if " " not in numbers_order:
    print("\nнет пробелов (введите числа, согласно условиям ввода.)")
    numbers_order = input('Введите целые числа через пробел: ')
if not is_int(numbers_order):
    print('\nвведены не цифры и не целые числа (введите числа, согласно условиям ввода.)\n')
    print(fail)
else:
    numbers_order = numbers_order.split()


# Меняем список строк на список чисел

list_numbers_order = [int(item) for item in numbers_order]


# Сортировка списка

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_numbers_order = merge_sort(list_numbers_order)

# Установка позиции элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.

print(f'Упорядоченный по возрастанию список: {list_numbers_order}')

if not binary_search(list_numbers_order, entered_number, 0, len(list_numbers_order)):
    rI = min(list_numbers_order, key=lambda x: (abs(x - entered_number), x))
    ind = list_numbers_order.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < entered_number:
        print(f'''Ближайший меньший элемент: {rI}, 
Ближайший больший элемент: {list_numbers_order[max_ind]} ''')
    elif min_ind < 0:
        print(f'''Ближайший больший элемент: {rI}, 
В списке нет меньшего элемента''')
    elif rI > entered_number:
        print(f'''Ближайший больший элемент: {rI}, 
Ближайший меньший элемент: {list_numbers_order[min_ind]} ''')
