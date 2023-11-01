from helpers import FileManagement
import pathlib


def print_menu():
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

def main():
        cwd = pathlib.Path.cwd()
        file_manager = FileManagement(cwd)
        while True:
            print(f"Текущий каталог: {file_manager.cwd}")
            print_menu()
            number = input("Введите свой выбор: ")

            if number == "1":
                file_manager.list_files()
            elif number == "2":
                file_manager.create_folder()
            elif number == "3":
                file_manager.delete_folder()
            elif number == "4":
                file_manager.rename_file()
            elif number == "5":
                file_manager.delete_folder()
            elif number == "6":
                file_manager.rename_file()
            elif number == "7":
                file_manager.show_image()
            elif number == "8":
                file_manager.change_directory()
            elif number == "0":
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

main()      


# if __name__ == "__run__":
#     run()


# file_manager = FileManagement("./")
# file_manager.run()
























# import helpers
# from helpers import FileManagement
# import pathlib
# cwd = FileManagement(pathlib.Path.cwd())
# user_input = FileManagement.welcome
# print(user_input)
# print("DIR", dir(cwd))
# match user_input:
#     case 1:
#         print("create a file")
#         cwd.create_file(input("Enter a destination foler"))
    
#     case 2:
#         print("deleting a file")
#         cwd.delete_file(input("Choose a file to delete"))
    
#     case 3:
#         print("Change a directory")