# File: app/io/output.py

def output_to_console(text):
    """
    Виводить текст на консоль.

    Args:
        text (str): Текст для відображення на консолі.
    """
    print(text)


def write_to_file(file_path, text):
    """
    Записує текст у файл за допомогою вбудованих методів Python.

    Args:
        file_path (str): Шлях до файлу для запису.
        text (str): Текст для запису у файл.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")
