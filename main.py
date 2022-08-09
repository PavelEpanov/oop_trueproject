class C:
    def meth(self, x):
        pass
    def meth(self, x, y, z): # Сработает только последний вариант, тк def объявляет ссылку на объект+
        pass

class X:
    def meth(self, *args):
        if len(args) == 1: # Ветвление по количеству аргументов
            pass
        if type(args[0]) == int: # Ветвление по типам аргументов(или isinstance)
            pass

# ВЫШЕПЕРЕЧИСЛЕННОЕ - ДЕЛАТЬ НЕЛЬЗЯ, ЭТО НЕ СТИЛЬ ПИТОНА
# нужно опираться на интерфейс объекта

class Y:
    def meth(self, x, y):
        x.operation() # Предположим, что x делает что - то правильное
