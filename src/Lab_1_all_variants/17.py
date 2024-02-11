def sorting_list(list_numbers):
    positive_num = list(filter(lambda n: n >= 0, list_numbers))
    negative_num = list(filter(lambda n: n < 0, list_numbers))
    list_numbers.clear()
    list_numbers.extend(positive_num)
    list_numbers.extend(negative_num)
    

def output_list(list_numbers):
    print("Результат работы программы:", ' '.join(map(str, list_numbers)))    
    

def input_list(list_numbers):
    input_string = input("Введите числа для сортировки, через пробел: ")
    numbers = input_string.split()
    for number in numbers:
        try:
            number = int(number)
            list_numbers.append(number)
        except ValueError:
            print("Вы ввели некорректные числа!")
            return 1
    return 0


def main():
    numbers = []
    if input_list(numbers) == 0:
        sorting_list(numbers)
        output_list(numbers)


if __name__ == '__main__':
    main()