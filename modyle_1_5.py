
immutable_var = (1, 2 ,'string1 ', 'string2')                # кортеж с числовым и строчным типом данных
print (immutable_var)                                        # выводим кортеж на экран
#immutable_var =( [1, 2 ,'string1 '], 'string2')             # в кортеже можно изменить только элементы списка[] так как список вложен в кортеж, а элементы кортежа изменить не получится , 'string2' -это вызовет ошибку (например, ссылку на один список ссылкой на другой).
#immutable_var [0][2] = 3                                    #
#print (immutable_var)                                       #
mutable_list = ([11,12,13,'eleven','twelve','thirteen'])       # переменной mutable_list присвоен список из нескольких элементов
#print (mutable_list)
mutable_list.append('new element')                           # добавление элемента в конец списка
del mutable_list[2:6]                                        # удаление элементов  3го 4го 5го
print (mutable_list)                                         # вывод на экран измененого списка