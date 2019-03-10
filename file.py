with open ('myfile.txt', 'r', encoding='utf-8') as myfile:
    for ln in myfile:
        ln = ln.upper()
        ln = ln.replace('\n', '')
        print(ln)

#r - просто читает файл
#w - перезаписывает файл
#a - добавляет в файл