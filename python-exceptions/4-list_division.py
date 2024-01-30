#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                a = my_list_1[i]
                b = my_list_2[i]
                result_list.append(a / b)
            except ZeroDivisionError:
                print("{}".format("division by 0"))
                result_list.append(0)
            except TypeError:
                print("{}".format("wrong type"))
                result_list.append(0)
            except IndexError:
                print("{}".format("out of range"))
                result_list.append(0)
    finally:
        return result_list
