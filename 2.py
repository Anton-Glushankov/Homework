print('Введите текст:')
text = "\n".join(iter(input, "")) # ввод текста завершается двойным enter

import string
text = text.translate(str.maketrans('', '', string.punctuation))
word_list = text.split()
print('Количество уникальных слов: ', len(set(word_list)))

max_len = 0
for word in word_list:
    if len(word) >= max_len:
        max_len = len(word)
        max_word = word     
print('Самое длинное слово: ', max_word)

from collections import Counter
text = text.replace(' ', '')
char_count = dict(Counter(text.lower()))
print('Частота букв: ', char_count)

# если в тексте несколько разных слов максимальный длины, данная программа вернет только одно из них
# если все же учитывать этот момент, можно сделать max_word сетом, куда добавятся все самые длинные слова, и вывести их все