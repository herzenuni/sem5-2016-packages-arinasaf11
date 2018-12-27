# Инвариантная самостоятельная работа

1.1 Исследовать функционал одного из модулей стандартной библиотеки (string, re, datetime, math, random, os, и т.д.) и, используя инструмент Jupyter Notebook, создать документ с описанием и примерами использования его функционала. Опубликовать его в портфолио.

1.2 Создание пользовательского пакета для приложения «Гостевая книга» («Регистрация на конференцию») с прототипами методов, позволяющих взаимодействовать с JSON-файлом (создание, удаление, переименование, чтение, запись).

Создаем модуль guestBook.py (Гостевая книга), где будет хранится наш класс GuestBook.
```python
class GuestBook:
    def __init__(self): #конструктор класса, где guests - это пустой список
        self.guests = list()

    def add_guest(self, name): #добавление гостя в книгу
        self.guests.append({"Guest_name": name})
        
    def delete_guest(self, name): #удаление гостя
        for guest in self.guests:
            if guest.get("Guest_name") == name:
                self.guests.remove(guest)

    def record_file(self): #запись данных в файл
        import json
        with open("./BookGuest.json", 'a') as file:
            data = {"List_of_guests": self.guests }
            json.dump(data, file) #json.dump- позволяет сохранять данные в json-файл

if __name__ == '__main__':
    guestbook = GuestBook()
    guestbook.add_guest('Arina')
    guestbook.add_guest('Kolya')
    guestbook.delete_guest('Kolya')
    guestbook.record_file()
```
В итоге у нас появляется файл с json-данными : GuestBook.json

```json
{
  "List_of_Guests": 
 [
   {
     "Guest_name": "Arina"
   }
 ]
}
```

Любая директория, содержащая файл  __init__.py, автоматически становится пакетом.
Для создания пакета необходимо создать этот файл.
Когда мы выполняем команду import <название_пакета> "выполняется" файл __init__.py.
Поэтому нам надо импортировать в __init__.py наш модуль.

```python
#Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
#sys.path.append - добавляет относительные пути для поиска модулей.
import sys
sys.path.append(get_script_dir())
from guestBook import GuestBook
#из файла guestBook импортируем модуль GuestBook
```
В результате мы сможем записывать и удалять имена в json-файле, импортируя папку package, в котором хранится наш пакет.

```python
import package
gb = package.GuestBook()
gb.add_guest("Egor")
gb.add_guest("Arina")
gb.add_guest("Nikita")
gb.delete_guest("Egor")
gb.record_file()
```

в папке, где находится запускаемый файл, создается GuestBook.json:

```json
{
   "List_of_guests": 
  [
    {
   "Guest_name": "Arina"
    }, 
    {
   "Guest_name": "Nikita"
    }
  ]
}
```
