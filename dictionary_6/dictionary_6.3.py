dictionary = {
    "строка": "простая последовательность символов",
    "метод Python": "действие, которое Python выполняет с данными",
    "пропуск": "непечатаемые символы такие, как пробелы, табуляции и символы" 
        " конца строки",
    "синтаксическая ошибка": "происходит тогда, когда Python не распознает"
        " часть программы как действительный код",
    "вещественные числа": "числа, имеющие дробную часть",
    "кортеж": "неизменяемый список"
}
print(dictionary)
print(f"Строка: \n\t{dictionary['строка']}\n")
print(f"Метод Python: \n\t{dictionary['метод Python']}\n")
print(f"Пропуск: \n\t{dictionary['пропуск']}\n")
print(f"Синтаксическая ошибка: \n\t{dictionary['синтаксическая ошибка']}\n")
print(f"Вещественные числа: \n\t{dictionary['вещественные числа']}\n")

for key, value in dictionary.items():
    print(f"{key.capitalize()}: \n\t{value}\n")
