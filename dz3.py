from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def details(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year: {self.year}')

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year
    
book1 = Book('Задача трех тел', 'Лю Цысинь', 2006)
book2 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1966)
book3 = Book('Убицы цветочной луны. Нефть. Деньги. Кровь.', 'Дэвид Гранн', 2017)

book1.details()
print(f'Age: {book1.age()} years\n')

book2.details()
print(f'Age: {book2.age()} years\n')

book3.details()
print(f'Age: {book3.age()} years\n')


'''
Создание класса и его экземпляров

1. Создайте класс `Book`, который будет представлять книгу. Класс должен иметь следующие атрибуты:

- `title` (название книги)
- `author` (автор книги)
- `year` (год издания)


2. Добавьте метод `details()`, который будет выводить информацию о книге в формате:

       
Title: [название книги]
Author: [автор книги]
Year: [год издания]


3. Создайте три экземпляра класса `Book` с разными параметрами (название, автор, год издания).
4. Выведите информацию о каждой книге, используя метод `details()`.
5. Дополнительно: добавьте метод `age()`, который будет возвращать возраст книги (текущий год минус год издания).
'''
