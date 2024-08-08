
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (s.lower() for s in list_to_search)


result1 = string_info("НУЖНО БОЛЬШЕ ЧИТАТЬ")
result2 = is_contains("не понимаю", ["Вообще Туго", "ПОМОГИТЕ", "SPAIN"])
result3 = string_info("Python ПОКА сложно")
result4 = is_contains("Связь", ["Джэк", "Медь*", "Адсл", "СкотчЛок"])


print("Результаты функции string_info:")
print(result1)
print(result3)


print("Результаты функции is_contains:")
print(result2)
print(result4)


print(f" {calls}")