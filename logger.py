from datetime import datetime as dt

def log_to_file(example, ans):
    time = dt.now().strftime('%D %H:%M')
    with open('Seminars\Seminar 8\log_of_examples.txt', 'a', encoding='utf-8') as file:
        file.write('Date created: {};\nЗадача: {};\nОтвет: {};\n  \n'
                    .format(time, example, ans))

def get_history():
    with open('Seminars\Seminar 8\log_of_examples.txt', 'r', encoding = 'utf-8') as file:
        history = file.read()
        return history