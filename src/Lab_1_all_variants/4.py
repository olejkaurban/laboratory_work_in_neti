def change_list(list_numbers):
    max_number = max(list_numbers)
    index_max_number = list_numbers.index(max_number)
    return max_number, index_max_number
    

def output_list(max_n, index_n):
    print(f"Максимальное число {max_n} под индексом {index_n}")
    
    
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
        max_n, index_n = change_list(numbers)
        output_list(max_n, index_n)


if __name__ == '__main__':
    main()