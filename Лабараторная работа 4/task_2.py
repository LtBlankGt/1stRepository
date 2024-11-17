import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT, OUTPUT, delimiter = ",", line_terminator = '\n') -> None:
    data = []
    with open(INPUT, 'r', newline = '') as f:
        reader = csv.DictReader(f, delimiter = delimiter)
        for string in reader:
            data.append(string)
    json_data = json.dumps(data, indent=4)

    with open(OUTPUT, "w") as f_out:
        f_out.write(json_data)






if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end = "")
