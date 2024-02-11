def change_list(list_numbers):
    below_0 = 0
    for number in list_numbers:
        if number < 0:
            below_0 +=1
    
    return below_0
    

def output_list(count):
    if count > 0:
        print(f"Результат работы программы: {count}", )
    else:
        print("В данной последовательности нет чисел удовлетворяющих условию.")
    

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
        output_list(change_list(numbers))


if __name__ == '__main__':
    main()