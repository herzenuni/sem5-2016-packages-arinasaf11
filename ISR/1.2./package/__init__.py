#Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
#sys.path.append - добавляет относительные пути для поиска модулей.
import sys
sys.path.append(get_script_dir())
from guestBook import GuestBook
#из файла guestBook импортируем модуль GuestBook
