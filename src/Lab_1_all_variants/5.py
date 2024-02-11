def change_list(list_numbers):
    min_number = min(list_numbers)
    index_min_number = list_numbers.index(min_number)
    return min_number, index_min_number
    

def output_list(min_n, index_n):
    print(f"Минимальное число {min_n} под индексом {index_n}")
    
    
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
        min_n, index_n = change_list(numbers)
        output_list(min_n, index_n)


if __name__ == '__main__':
    main()