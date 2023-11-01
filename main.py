from helpers import FileManagement
import pathlib
cwd = pathlib.Path().resolve()
file_manager = FileManagement(cwd)
file_manager.run()

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