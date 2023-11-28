import os

def gen_files_path(path: str = os.path.join('..')) -> list[str]:
    return [os.path.join(root, file_name) for root, dirs, files in os.walk(path) for file_name in files]

print(gen_files_path())

user_path = input('Укажите путь до каталога: ')
print(gen_files_path(user_path))