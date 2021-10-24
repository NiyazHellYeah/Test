# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list1 = []
b = int(input('Введите количество элементов: '))
for i in range(b):
    list1.append(input('Введите элемент: '))
print(list1)
a = None
if len(list1) % 2 == 1:
    a = list1.pop()
list2 = []
if a != None:
    list2.append(a)

n = 0
while n != len(list1):
    list2.insert(n, list1[n + 1])
    list2.insert(n + 1, list1[n])
    n += 2

print(list2)
