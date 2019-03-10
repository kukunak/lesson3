#Скачайте файл по ссылке
#Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open ('referat.txt', 'r', encoding='utf-8') as ref:
    content = ref.read()
    print(len(content))
    words = content.split()
    print(len(words))
    content = content.replace('.', '!')
with open ('referat2.txt', 'w', encoding='utf-8') as ref:
    new = ref.write(content)
