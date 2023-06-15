# Шаблон 22 задания

dic = {} # Словарь

for line in open('22.txt'):
    array = [int(x) for x in line.replace(';', ' ').split()] # Строка в виде массива: 0 индекс - свое id, 1+ индексы - остальное
    dic[array[0]] = array[1:] # ключ: id процессора, значение: 0 индекс - свое время, 1+ индексы - id чужих процессов

def time(key): 
    if dic[key][1] == 0: return dic[key][0] # Если нет чужих процессоров, то время = свое время
    else: return dic[key][0] + max(time(otherKey) for otherKey in dic[key][1:]) # Если зависимые процессоры есть,
    # то, возращаем свое время + максимум от времен зависимых процессоров

ar = [time(key) for key in dic.keys()] # Находим максимум времени всех процессоров
print(len([x for x in ar if x <= 300]))