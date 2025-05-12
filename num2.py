def analyze_dictionary():
    
    sample_dict = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
    
    dict_keys = set(sample_dict.keys())
    dict_values = set(sample_dict.values())
    
    keys_values_union = dict_keys.union(dict_values)
    
    print("Анализ словаря:")
    print(f"• Ключи: {dict_keys}")
    print(f"• Значения: {dict_values}")
    print(f"• Объединение ключей и значений: {keys_values_union}")

analyze_dictionary()