# Шаблон для задания 8
from itertools import *


# Количество слов
answer = 0

for word in product(...., repeat=...): # Буквы и кол-во букв в слове
    word = ''.join(word)

    if .....: # Условие
        answer += 1

print(answer)



# Список слов
count = 1

for word in product(...., repeat=...): # Буквы и кол-во букв в слове
    # Буквы пишем в порядке списка примера (не условия)
    word = ''.join(word)

    if .....: # Условие
        print(word, count)

    count += 1
