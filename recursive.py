# Эта программа содержит рекурсивную функцию.
def main():
    # Сообщение будет показано 5 раз.
    message(5)


def message(times):
    if times > 0:
        print('Это рекурсивная функция, номер ', times)
        message(times - 1)


main()
