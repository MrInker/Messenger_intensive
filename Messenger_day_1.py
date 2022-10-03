import datetime
from datetime import timezone

# ЯДРО! Отправка и получение сообщений!
# Мессенджер!

# все сообщения хроанить в СПИСКЕ

all_messages = []
delta_tz = datetime.timedelta(hours=3, minutes=0)
dtime = datetime.datetime.now(timezone.utc) + delta_tz


# Функция добавления сообщений
# def - объявление финкции
# sender - кто отправил сообщение
# text - текст сообщения
def add_message(sender, text):
    new_message = {
        "sender": sender,
        "message": text,
        "time": dtime.strftime("Дата: %d/%m/%Y  время: %H:%M:%S")
        # ToDO Задание: подставлять текущее время (datatime / strftime)
    }
    #  append - добавление лемента в конец
    if len(all_messages) == 100:
        del all_messages[0]
    all_messages.append(new_message)  # Добавляем new_message в конец списка all_messages


# Для проверки заполняем с ловарь на 150 записей:
for i in range(150):
    add_message(str(i), str(i))


# add_message("Mike", "Питон - это пиздец как круто")
# add_message("Павел", "Питон - это реально")
# add_message("Жека", "Питон - просто огнищще")
# add_message("Коржик", "Питон - не ява")


# Func для вывода сообщения на экран
# mess - сообщение {sendet, text, time}
def print_message(mess):
    print(mess['sender'])
    print(mess['message'])
    print(mess['time'])


# ИЛИ

def print_msg(message):
    # [sender]: text / time
    print(f"Имя:[{message['sender']}] Сообщение: \"{message['message']}\"  ({message['time']}) ")


# вывести 0-е сообщение на экран
#print_message(all_messages[0])

print('0й элемент Словаря: ', end='')
print_msg(all_messages[0])
print('100й элемент Словаря: ', end='')
print_msg(all_messages[99])

print('Длинна массива: ', len(all_messages))
# Выводим все сообщения
# for - цикл выведет все сообщения

# для каждого сообщения в списке сообщений - сделать следующее (напечатать сообщение print_message(msg))

for msg in all_messages:  # для каждого сообщения в списке сообщений
    print_msg(msg)  # переменная msg хранит по очереди каждое из сообщений (1,2,3,...)
