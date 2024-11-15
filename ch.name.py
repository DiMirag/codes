import os

# Путь к папке с файлами
folder_path = "/путь/к/вашей/папке"

# Префикс или суффикс, который хотите добавить (оставьте пустым, если не нужен)
prefix = "NewPrefix_"  # Пример: добавит "NewPrefix_" в начало имени файла
suffix = "_NewSuffix"  # Пример: добавит "_NewSuffix" в конец имени файла

# Функция переименования файлов
def rename_files(folder_path, prefix="", suffix=""):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        # Проверяем, что это файл, а не папка
        if os.path.isfile(old_path):
            # Получаем имя файла и его расширение
            name, ext = os.path.splitext(filename)
            # Создаем новое имя
            new_name = f"{prefix}{name}{suffix}{ext}"
            new_path = os.path.join(folder_path, new_name)
            
            # Переименовываем файл
            os.rename(old_path, new_path)
            print(f"{filename} -> {new_name}")

# Запуск функции
rename_files(folder_path, prefix=prefix, suffix=suffix)
