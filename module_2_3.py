my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero_ = 0

while zero_ < len(my_list) :
    if my_list[zero_] == 0 :
        zero_ += 1
        continue
    if my_list[zero_] < 0 :
        break
    print (my_list[zero_])
    zero_ += 1


















