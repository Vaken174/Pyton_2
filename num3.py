def find_common_elements():
    
    first_list = list(map(int, input("Введите числа первого списка через пробел: ").split()))
    second_list = list(map(int, input("Введите числа второго списка через пробел: ").split()))
    
    common_elements = sorted(set(first_list) & set(second_list))
    
    if common_elements:
        print("Общие элементы:", ", ".join(map(str, common_elements)))
    else:
        print("Общих элементов не найдено.")

find_common_elements()