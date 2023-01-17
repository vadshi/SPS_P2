"""
links: https://stackoverflow.com/questions/14588905/how-to-get-instance-given-a-method-of-the-instance

"""
#
#
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print('Class Foo:', self.name)
#
#     def change(self):
#         self.name += ' change!'
#
#
# # Создаем экземпляры класса
# A = Foo('A')
# B = Foo('B')
#
#
# # Вызов метода say()
# A.say()
# B.say()
# print(f'{id(A) = }')
# # ВАЖНО, создаем еще один объект, а не ссылку!
# S = A.say
# C = A.change
#
# print(S is A.say)  # id(S) == id(A.say)
# print(type(S), type(A.say))
# print(id(S), id(A.say))
# print(hex(id(Foo.say)).upper())
# print(hex(id(S)).upper())
# print(hex(id(A.say)).upper())
# print(S)
# print(vars(S))
# print(A.say)
# # Вызываем
# S()
# C()
# print(A.name)
# # Меняем значение для 'say'
# A.say = "Теперь это значение метода 'say' для A"
# print(A.say)
# #
# # Пытаемся вызвать метод say() у экземпляра A
# try:
#     A.say()
# except TypeError:
#     print('Wrong method')
#
# del A
# # Вызов метода у экземпляра B
# B.say()
# print(id(B.say))
#
# # Вызов как функции
# S()
# C()
# S()
# print(S.__self__)
# A = S.__self__   # Ссылка на первоначальный экземпляр
# del A.say
# A.say()
# print(f'{id(A) = }')
# print(f'{id(A.say) = }')
# print(f'{id(S) = }')
# print(type(S))
# Foo.say(A)
#
# # Для класса (здесь ссылка!)
# print(f'{id(Foo.say) = }')
# D_link = Foo.say
# print(f'{id(D_link) = }')
# D_link(Foo('D'))  # Foo.say(Foo instance) Out: ???
# # Тот же самый механизм, но для экземпляра Foo('D')
# Foo.say(A)
# print(type(D_link))
# print(D_link.__name__)
# D_link(B)  # work Class Foo: B
# D_link(A)  # work Class Foo: A
#
# # Удаляем в классе
# del Foo.say
# # B.say()  # Error -> Foo.say(B)
# D_link(B)  # work
#
#
# # Вызываемый объект или нет
# print(callable(D_link))
# print(callable(A.name))
# a = 5
# print(callable(a))
# print(callable(Foo))

