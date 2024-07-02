def main():
    try:
        num1 = int(input('Ввидите первое число: '))
        num2 = int(input('Ввидите второе число: '))

        result = num1 / num2

    except ValueError:
        print('Ошибка: Введено не числовое значение.')
    except ZeroDivisionError:
        print('Ошибка: Деление на ноль невозможно.')
    else:
        print(f'Ответ: {result}')

    finally:
        print('Сайга далуг динакх ас')

if __name__ == '__main__':
    main()