def user_name():
    try:
        name = input('Напишите ваше имя: ')
        if not name:
            raise ValueError('Имя не может быть пустым.')
        return name
    except ValueError as ve:
        print(f'Ошибка: {ve}')
        return None
    
def main():
    name = None
    while name is None:
        name = user_name()
    print(f'Привет, {name}!')

if __name__ == '__main__':
    main()

'''
Повторение функций input() и print() c try-except

Напишите программу, которая запрашивает у пользователя 
его имя с помощью функции input() и затем выводит приветственное 
сообщение на экран с использованием функции print(). 
Пример вывода: "Привет, Иван!"
'''