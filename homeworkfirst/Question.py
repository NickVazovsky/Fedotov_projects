while(True):
    first = input("Какой язык мы изучаем:")
    if(first=="Python" or first == "python"):
        print("Ответ правильный")
    else:
        print("Ответ не верный")
    second = input("Какая команда выводит сообщения на экран:")
    if(second == "print" or second == "Print"):
        print("Ответ верный")
    else:
        print("ответ не верный")
    third = input("0 является True или False:")
    if(third == "False" or third == "false"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    four = input("Целочисленный тип в Python это:")
    if(four == "int" or four == "Int"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    five = input("Как обозначается ложь в Python:")
    if(five == "False" or five == "false"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Six = input("Как обозначается истина в Python:")
    if(Six == "True" or Six =="true"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Seven = input("как называется цикл с пред-условием:")
    if(Seven == "while" or Seven == "While"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Eight = input("Как называется \"перебирающий\" цикл:")
    if(Eight == "for" or Eight == "For"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Nine = input("Какая команда формирует список:")
    if(Nine == "list" or Nine == "List"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Ten = input("Какое ключевое слово используется для определения функции:")
    if(Ten == "def" or Ten == "Def"):
        print("Ответ верный")
    else:
        print("Ответ не верный")
    Restart = input("Хотите повторить тест отвечать нужно да или нет")
    if(Restart == "да" or Restart == "Да"):
         continue
    else:
        print("Спасибо за пройденный тест!")
        break

