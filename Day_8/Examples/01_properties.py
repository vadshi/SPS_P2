class StudentA:
    """ Test class for learning """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name
    
    def set_name(self, value):
        print('From set_name()')
        self._name = value

    def del_name(self):
        self._name = ''

    # V1
    # Для чтения(getter) -> get_name, для изменения(setter) -> set_name, для удаления(deleter) -> del_name
    # name = property(fget=get_name, fset=set_name, fdel=del_name)
    # For example: print(student.name); student.name = 12; del student.name
    
    # V2
    # name = property()
    # print(type(name))
    # print(dir(name))
    # name = name.getter(get_name)
    # name = name.setter(set_name)
    # name = name.deleter(del_name)
    
    # V3
    # Первый аргумент - это getter(считать значение)
    # name = property(get_name)
    # name = name.setter(set_name)
    # name = name.deleter(del_name)


# student = StudentA('first')
# print(student.__dict__)
# print(student.name)        # fget=get_name
#
# # присвоить новое значение
# student.name = 'second'  # fset=set_name
# print(student.name)
# print(student.__dict__)
#
# del student.name        # fdel=del_name
# print(student.__dict__)
# print(student.name)
# student.name = 'third'
# print(student.__dict__)
# print(student.name)
# print(student._name)
# print(type(student.name))
# print('*' * 40)


# Обычно property используют как декоратор
class StudentB:
    '''Test class for learning'''
    def __init__(self, name):
        self._name = name

    @property   # student.name(реализован getter)
    def name(self):
        return self._name

    # student.name = 12(реализован setter)
    # мы должны явно указать имя аттрибута, для которого указываем setter
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            raise Exception('Too small')

    # del student.name (реализован deleter)
    # мы должны явно указать имя аттрибута, для которого указываем deleter
    @name.deleter
    def name(self):
        self._name = ''


s_b = StudentB('Python')
# print(s_b.__dict__)

print(s_b.name, type(s_b.name)) # Результат работы getter'а
# print(s_b.name())   # TypeError: 'str' object is not callable

s_b.name = 'Java'  # Результат работы setter'а
print(s_b.__dict__)
print(s_b.name)

del s_b.name     # Результат работы deleter'а
print(s_b.__dict__)
print(f'{s_b.name!r}')

# В setter есть проверка данных
s_b.name = 'go'  # error Exception: Too small
