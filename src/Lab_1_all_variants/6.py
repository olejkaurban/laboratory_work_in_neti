def change_list(list_numbers):
    positive_num = list(filter(lambda n: n >= 0, list_numbers))
    if len(positive_num) != 0:
        min_number = min(positive_num)
    else:
        min_number = "non"
    return min_number
    

def output_list(number):
    if number != "non":
        print(f"Результат работы программы: {number}")    
    else:
        print("В данной последовательности нет чисел удовлетворяющих условию.")
2
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