def main():
    shopping_list =[]
    print('Введите список покупок.')

    while True:
        item = input('Введите покупки: ')
        if item == '':
            break
        shopping_list.append(item)

    with open('shopping_list.txt', 'w', encoding='utf-8') as file:
        for item in shopping_list:
            file.write(item + '\n')

    print('Список покупок сохранен в файле "shopping_list.txt".')

if __name__ == '__main__':
    main()

'''
Задание на запись в файл:


Создайте программу на Python, которая просит пользователя ввести 
список покупок. После ввода всех покупок программа должна записать 
их в текстовый файл "shopping_list.txt" так, чтобы каждый элемент 
списка был записан на отдельной строке. Затем программа должна вывести 
сообщение об успешном сохранении списка.

Например, если пользователь введет следующий список покупок:

    
    Хлеб

    Молоко

    Яйца

    Сахар   

То содержимое файла "shopping_list.txt" должно выглядеть так:


    Хлеб

    Молоко

    Яйца

    Сахар

     
После этого программа должна вывести сообщение:

Список покупок успешно сохранен в файле "shopping_list.txt".
'''