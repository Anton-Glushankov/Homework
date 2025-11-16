data = [' Иван Иванов ', 'Петров;Петр ', 'Сидорова Анна ', ' ОЛЕГ КУЗНЕЦОВ ', 'МАРИЯ; ТРОФИМОВА']

import re

clear_data = [re.sub(r'[^а-яА-Я]', ' ', item) for item in data]
clear_data = [re.sub(r'\s+', ' ', item) for item in clear_data]
clear_data = [item.strip().lower().title() for item in clear_data]
new_data = []
for i in range(len(clear_data)):
    words = clear_data[i].split()
    if len(words[0]) > len(words[1]):
        words[0], words[1] = words[1], words[0]
    new_str = ' '.join(words)
    new_data.append(new_str)
    
print(new_data)
