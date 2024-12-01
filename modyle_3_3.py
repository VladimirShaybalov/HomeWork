def print_params(a = 1, b = 'строка', c = True ):
    print(a, b, c,)

values_list=[2,'string',False]
values_dict={'a':12, 'b':'строка', 'c': False}
values_list_2 =[54.32,'Строка']

print_params()
print_params(values_list,str(values_dict) ,True)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)
