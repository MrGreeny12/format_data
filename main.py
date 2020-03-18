# Домашнее задание к лекции 3.1 «Работа с разными форматами данных» Взять из папки 3.1.formats.json.xml файлы с новостями newsafr.json и newsafr.xml

# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

# Задача №1 Написать программу для файла в формате json.

# Задача №2. Написать программу для файла в формате xml.

def read_json_files(name):
    '''Функция чтения файлов формата json'''
    import json
    import chardet

    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = json.loads(data)
        original_text = ''
        for items in data['rss']['channel']['items']:
            original_text += ' ' + items['description']
        return original_text


def read_xml_files(name):
    '''Функция чтения файлов формата xml'''
    import xml.etree.cElementTree as ET

    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    items = root.findall('channel/item')
    original_text = ''
    for item in items:
        original_text += ' ' + item.find('description').text
    return original_text


def word_count(original_text):
    '''функция по отбору слов длиной больше 6 символов'''
    item_list = original_text.split(' ')
    item_set = set()
    for i in item_list:
        if len(i) > 6:
            item_set.add(i)
    word_value = {}
    for i in item_set:
        count = 0
        for j in item_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value  # возвращаем словарь {слово:количество}


def top10(word_value):
    '''функция по созданию топ-10'''
    register = list()
    l_dict = str(len(word_value))
    for i in word_value.items():
        l_word = str(i[1])
        register.append((len(l_dict) - len(l_word)) * '0' + str(i[1]) + ' ' + i[
            0])  # разворачиваем и добавляем нули перед количеством для сортировка, делаем слияние элементов = '00012 слово'
    register.sort(reverse=True)
    top_10 = {}
    count = 1
    for j in register:
        top_10[count] = j.split(' ')  # получаем словарь типа {1: (количество, слово)}
        top_10[count][0] = int(top_10[count][0])
        if count == 10:
            break
        count += 1
    return top_10  # возвращаем отсортированный словарь ТОП-10 {номер: (количеств, слово)}
    pprint(top10)


def main():  # в конце
    '''базовая функция'''
    while True:
        comand_name = input('Введите команду: j - newsafr.json, x - newsafr.xml, для выхода введите: exit : ')
        if comand_name == 'j':
            print('Идет обработка файла ...')
            top_10 = top10(word_count(read_json_files('newsafr.json')))
            for k in top_10.values():
                print(k[0], ': ', k[1])
        elif comand_name == 'x':
            print('Идет обработка файла ...')
            top_10 = top10(word_count(read_xml_files('newsafr.xml')))
            for k in top_10.values():
                print(k[0], ': ', k[1])
        elif comand_name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')


main()
