def change_list(list_numbers):
    tuple_numbers = tuple(list_numbers)
    new_list = []
    for item in range(0, len(tuple_numbers), 2):
        new_list.append(tuple_numbers[item])
        
    return new_list
    

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
        new_list = change_list(numbers)
        output_list(new_list)


if __name__ == '__main__':
    main()