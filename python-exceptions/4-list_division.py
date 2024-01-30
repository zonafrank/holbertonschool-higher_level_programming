#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
            result_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
    return result_list
