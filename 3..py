# Написать функцию,
# принимающую произвольное кол-во чисел и возвращающую кортеж всех целых чисел,
# т.е. все дробные значения отсеиваются функцией.

def Function(*args):
    lst = list(args)
    for s in lst[:]:
        if type(s) == float:
            lst.remove(s)
    return tuple(lst)

print(Function(2.5, 6.2, 87, 0.5, 90.2, 7))

