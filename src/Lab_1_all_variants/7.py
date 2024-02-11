def change_list(list_numbers):
    new_list = []
    for i in range(len(list_numbers)):
        if list_numbers[i] > 0 and list_numbers[i] < 1:
            new_list.append(i)
    list_numbers.clear()
    list_numbers.extend(new_list)
    

def output_list(list_numbers):
    if len(list_numbers) > 0:
        print("Результат работы программы:", ' '.join(map(str, list_numbers)))    
    else:
        print("В данной последовательности нет чисел удовлетворяющих условию.")
2
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
        output_list((numbers))


if __name__ == '__main__':
    main()