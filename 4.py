text = input('Введите строку на русском языке: ')
new_text = ''
i = 0
while i < len(text):
    match text[i]:
        case 'а':
            new_text += 'е'
        case 'е':
            new_text += 'ё'
        case 'ё':
            new_text += 'и'
        case 'и':
            new_text += 'о'
        case 'о':
            new_text += 'у'
        case 'у':
            new_text += 'ы'
        case 'ы':
            new_text += 'э'
        case 'э':
            new_text += 'ю'
        case 'ю':
            new_text += 'я'
        case 'я':
            new_text += 'а'
        case _:
            new_text += text[i]
    i += 1
print(new_text)
