# File: app/io/input.py

def read_console_input():
    """
    Читає ввдені корситувачем дані

    Returns:
        str: Рядок введений користувачем
    """
    return input("Enter text: ")


def read_file_python(file_path):
    """
    Читає з файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): Шлях до файлу для читання.

    Returns:
        str: Вміст файлу або повідомлення про помилку, якщо файл неможливо прочитати.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"


def read_file_pandas(file_path):
    """
    Читає вміст із файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до файлу для читання.

    Returns:
        pandas.DataFrame or str: DataFrame з даними файлу в разі успіху,
                                 або повідомлення про помилку, якщо станеться виняток.
    """
    import pandas as pd
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return f"Error reading file with pandas: {e}"
