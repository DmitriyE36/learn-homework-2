"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        f_length = len(content)
        print(f'Длина строки: {f_length} символов')
        f_quantity = len(content.split())
        print(f'Количествл слов в тексте: {f_quantity}')
        new_text = content.replace(".", "!")
        print(new_text)
        with open('referat2.txt', 'w', encoding='utf-8') as new_f:
            new_f.write(new_text)
    
if __name__ == "__main__":
    main()
