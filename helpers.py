import os
from helpers import FileManagement
import pathlib
from pathlib import Path

class FileManagement:
    def init(self, cwd):
        self.cwd = cwd
    
    def print_menu(self):
        print("========================================")
        print("1️ Список файлов в текущем каталоге")
        print("2️ Создание нового файла")
        print("3️ Создание новой папки")
        print("4️ Удаление файла")
        print("5️ Удаление папки")
        print("6️ Переименование файла или папки")
        print("7️ Отображение изображения")
        print("8️ Изменение текущей папки")
        print("0️ Выход")
        print("========================================")

    def list_files(self):
        print(f"Listing files at {self.cwd}")
        files = os.listdir(self.cwd)
        for file in files:
            print(file)
            
    def create_folder(self):
        folder_name = input("Введите имя новой папки: ")
        folder_path = os.path.join(self.cwd, folder_name)
        os.mkdir(folder_path)
        print(f"Создана новая папка: {folder_path}")
        
    def delete_folder(self):
        folder_name = input("Введите имя папки, которую нужно удалить: ")
        folder_path = os.path.join(self.cwd, folder_name)
        os.rmdir(folder_path)
        print(f"Удалена папка: {folder_path}")
        
    def move_folder(self):
        folder_name = input("Введите имя папки, которую нужно переместить: ")
        new_folder_name = input("Введите новое имя папки: ")
        folder_path = os.path.join(self.cwd, folder_name)
        new_folder_path = os.path.join(self.cwd, new_folder_name)
        os.rename(folder_path, new_folder_path)
        print(f"Перемещена папка: {folder_path} -> {new_folder_path}")
        
    def rename_file(self):
        file_name = input("Введите имя файла, который нужно переименовать: ")
        new_file_name = input("Введите новое имя файла: ")
        file_path = os.path.join(self.cwd, file_name)
        new_file_path = os.path.join(self.cwd, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Переименован файл: {file_path} -> {new_file_path}")
        
    def open_file(self):
        file_name = input("Введите имя файла, который нужно открыть: ")
        file_path = os.path.join(self.cwd, file_name)
        print(f"Открывается файл: {file_path}")
       
        
    def edit_file(self):
        file_name = input("Введите имя файла, который нужно отредактировать: ")
        file_path = os.path.join(self.cwd, file_name)
        print(f"Редактируется файл: {file_path}")
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            
            print("Содержимое файла:")
            print(content)
            
            new_content = input("Введите новое содержимое файла: ")
            
            with open(file_path, 'w') as file:
                file.write(new_content)
            
            print("Файл успешно отредактирован.")
        
        except FileNotFoundError:
            print("Файл не найден.")
            
    def change_directory(self):
        new_directory = input("Введите новую директорию: ")
        self.cwd = new_directory
        print(f"Текущая директория изменена на: {new_directory}")

    def run(self):
        while True:
            print(f"Текущий каталог: {self.cwd}")
            self.print_menu()
            number = input("Введите свой выбор: ")

            if number == "1":
                self.list_files()
            elif number == "2":
                self.create_folder()
            elif number == "3":
                self.delete_folder()
            elif number == "4":
                self.rename_file()
            elif number == "5":
                self.delete_folder()
            elif number == "6":
                self.rename_file()
            elif number == "7":
                self.show_image()
            elif number == "8":
                self.change_directory()
            elif number == "0":
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
        
        file_manager = FileManagement("./")
        file_manager.run()