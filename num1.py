def calculate_powers():
    
    input_values = input("Введите числа или строки через пробел: ")
    values_list = input_values.split()
    exponent = int(input("Введите степень: "))
    results = []

    for value in values_list:
        try:
            number = float(value)
            
            if number.is_integer():
                number = int(number)
                
            powered_value = number ** exponent
            results.append(str(powered_value))
        except ValueError:

            repeated_string = value * exponent
            results.append(repeated_string)
            
    print("Результат:", " ".join(results))

calculate_powers()