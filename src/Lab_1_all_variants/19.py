def sorting_list(list_numbers):
    new_list = [0] * len(list_numbers)
    for i in range(len(list_numbers)):
        new_list[i] = list_numbers[len(list_numbers) - i -1]
    list_numbers.clear()
    list_numbers.extend(new_list)
    

def output_list(list_numbers):
    print("Результат работы программы:", ' '.join(map(str, list_numbers)))
    

def input_list(list_numbers):
    input_string = input("Введите числа через пробел: ")
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