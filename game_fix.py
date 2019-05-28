import time

x = "X"
y = "Y"
empty = " "
draw = "Ничья"
num_kvadrat = 9


def ask_xod(question):  # Задаем вопрос. Ответ да или нет
    respons = None
    while respons not in ("y", "n"):
        respons = input(question).lower()

    return respons


def ask_number(question, low, high):  # Запрашиваем о вводе числа в заданном диапозоне
    respons = None
    while respons not in range(low, high):
        respons = int(input(question))

    return respons


def tip_fishki():  # Определяем типы фишек компьютера и игрока
    first = ask_xod("Хочешь оставить за собой первый ход? (y/n): ")
    if first == "y":
        print("\n Ну что ж, даю тебе фору: играй крестиками.")
        human = x
        computer = 0
    else:
        print("\n Ха... Буду начинать я.")
        human = 0
        computer = x

    return computer, human


def new_dosk():  # Создаем новую доску
    dosk = []
    for __ in range(num_kvadrat):
        dosk.append(empty)

    return dosk


def display_dosk(dosk):  # Выводим доску
    print("\n\t", dosk[0], "|", dosk[1], "|", dosk[2])
    print("\t", "---------")
    print("\n\t", dosk[3], "|", dosk[4], "|", dosk[5])
    print("\t", "---------")
    print("\n\t", dosk[6], "|", dosk[7], "|", dosk[8], "\n")


def dopystimie_xod(dosk):  # Возвращаем список доступных ходов
    xod = []  # создали список
    for kvadrat in range(num_kvadrat):  # выводим каждый из элементов
        if dosk[kvadrat] == empty:  # если в доске число равно пустоте
            xod.append(kvadrat)  # в список добавляем число
    return xod


def pobediteli(dosk):  # Возвращаем победителя игры
    pobedi = ((0, 1, 2),  # записываем все возмозжые способы победы
              (3, 4, 5),
              (6, 7, 8),
              (0, 3, 6),
              (1, 4, 7),
              (2, 5, 8),
              (0, 4, 8),
              (2, 4, 6),)
    for row in pobedi:  # выводим каждый из элементов
        if dosk[row[0]] == dosk[row[1]] == dosk[row[2]] != empty:  # если три числа ровны между собой и не ровны пустоте
            pobediteli = dosk[row[0]]  # записываем в переменную одну из фишек выигранного ряда
            return pobediteli  # возвращяем переменную
        if empty not in dosk:  # если постоты нет в доске
            return draw  # возвращяем переменную

    return None


def human_move(dosk, human):  # Возвращаем номер поля, на которое игрок хочет поставить фишку
    legal = dopystimie_xod(dosk)  # список допустимых ходов
    move = None
    while move not in legal:  # пока пользов. не введет одно из чисел этого списка
        move = ask_number("Выбери одно из полей <0 - 8>: ", 0, num_kvadrat)  # спрашиваем его
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")

    print("Ладно...")
    time.sleep(2)
    return move


def computer_move(dosk, computer, human):  # Возвращаем ход компьютера
    dosk = dosk[:]
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in dopystimie_xod(dosk):  # цикл помещает крестик или нолик и проверяет, не ведет данный ход к победе.
        dosk[move] = computer
        if pobediteli(dosk) == computer:  # если след ходом может победить компьютер, выбираем этот ход
            print(move)
            return move
        dosk[move] = empty  # отменим внесенные изменения

    for move in dopystimie_xod(dosk):
        dosk[move] = human
        if pobediteli(dosk) == human:  # если след ходом может победить человек, блокируем этот ход
            print(move)
            return move
        dosk[move] = empty  # отменим внесенные изменения

    for move in best_moves:  # поскольку след ходом ни одна сторона не может победить, выберем лучшее из доступных полей
        if move in dopystimie_xod(dosk):
            print(move)
            return move


def next_turn(turn):  # Возвращаем тип фишки след хода
    if turn == x:
        return 0
    else:
        return x


def victory_draww(the_pobediteli, computer, human):  # Вызывается если один из противников добился победы или если
    # игра закончилась вничью
    if the_pobediteli != draw:
        print("Три", the_pobediteli, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_pobediteli == computer:
        print("Победа осталась за мной!")
    elif the_pobediteli == human:
        print("О нет, этого не может быть!\n "
              "Клянусь: я компьютер, не допущу этого больше!\n")
    elif the_pobediteli == draw:
        print("Тебе несказанно повезло, дружок: ты сумел свести игру вничью!")


def main():
    computer, human =  tip_fishki()
    turn = x
    dosk = new_dosk()
    display_dosk(dosk)
    while not pobediteli(dosk):
        if turn == human:
            move = human_move(dosk, human)
            dosk[move] = human
        else:
            move = computer_move(dosk, computer, human)
            dosk[move] = computer
        display_dosk(dosk)
        turn = next_turn(turn)
    the_pobediteli = pobediteli(dosk)
    victory_draww(the_pobediteli, computer, human)

main()
print("\n\nНажмите Enter, чтобы выйти.")
