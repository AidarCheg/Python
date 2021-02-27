import os, os.path, mimetypes, time
from os import path

file_name = str(input("Введите название файла:\t"))

if open(file_name):
	print("\nФайл найден!\n")

	size = os.path.getsize(file_name)
	print("Размер файла:\t"+ str(size) + " kb")

	direct = os.path.abspath(file_name)
	print("Полный путь:" + str(direct))

	full_name = path.basename(r'C:\Users\Aigap\OneDrive\Документы\python.py ')
	name = path.splitext(full_name)[1]
	print("Расширение файла:\t"+str(name))

	last_mod = time.ctime(os.path.getmtime(file_name))
	created = time.ctime(os.path.getctime(file_name))

	print("Последняя модификация:\t" + str(last_mod))
	print("Дата создания:\t" + str(created))
else:
	print("Файл не найден!")   