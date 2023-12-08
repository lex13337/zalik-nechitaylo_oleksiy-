# оголошення функції для заміни слова у текстовому файлі
def zamina_slova(slyahdofile, word1, word2):
    try:
        # відкриття файлу для читання з кодуванням UTF-8
        with open(slyahdofile, 'r', encoding='utf-8') as file:
            # зчитування тексту з файлу
            text = file.read()

        # заміна word1 на word2 у тексті
        changed_text = text.replace(word1, word2)

        # відкриття файлу для запису з кодуванням UTF-8
        with open(slyahdofile, 'w', encoding='utf-8') as file:
            # Запис зміненого тексту у файл
            file.write(changed_text)

        # виведення повідомлення про успішну заміну
        print(f'Заміна слова успішна: {word1} -> {word2}')

    except FileNotFoundError:
        # виведення повідомлення про помилку, якщо файл не знайдено
        print(f'Error: Файл "{slyahdofile}" не знайдено.')


# зчитування шляху до текстового файлу, слова для заміни та нового слова від користувача
slyahdofile = input('Надайте шлях до файлу (C:/Users/...): ')
word1 = input('Слово яке потрібно замінити: ')
word2 = input('Слово на яке потрібно замінити: ')

# виклик функції для заміни слова у вказаному файлі
zamina_slova(slyahdofile, word1, word2)