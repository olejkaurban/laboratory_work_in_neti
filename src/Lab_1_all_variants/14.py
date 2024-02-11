def change_list(list_numbers):
    min_number = min(list_numbers)
    list_numbers[list_numbers.index(min_number)] = list_numbers[0]
    list_numbers[0] = min_number
    

def output_list(list_numbers):
    print("Результат работы программы:", ' '.join(map(str, list_numbers)))    
    

def input_list(list_numbers):
    input_string = input("Введите числа через пробел: ")
    numbers = input_string.split()
    for number in numbers:
        try:
            number = float(number)
            list_numbers.append(number)
        except ValueError:
            print("Вы ввели некорректные числа!")
            return 1
    return 0


def main():
    numbers = []
    if input_list(numbers) == 0:
        change_list(numbers)
        output_list(numbers)


if __name__ == '__main__':
    main()