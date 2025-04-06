# File: main.py

from app.io import input as io_input
from app.io import output as io_output


def main():

    console_text = io_input.read_console_input()
    io_output.output_to_console("You entered: " + console_text)


    file_path = 'data/sample.txt'
    file_content_python = io_input.read_file_python(file_path)
    io_output.output_to_console("Content read using built-in method:\n" + file_content_python)

    io_output.write_to_file('data/output_builtin.txt', file_content_python)

    file_path_csv = 'data/sample.csv'
    file_content_pandas = io_input.read_file_pandas(file_path_csv)
    io_output.output_to_console("Content read using pandas:")
    io_output.output_to_console(str(file_content_pandas))

    if hasattr(file_content_pandas, 'to_csv'):
        try:
            file_content_pandas.to_csv('data/output_pandas.csv', index=False)
        except Exception as e:
            io_output.output_to_console(f"Error writing pandas output: {e}")


if __name__ == "__main__":
    main()
