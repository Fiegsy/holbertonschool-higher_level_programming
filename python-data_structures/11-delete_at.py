#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    return my_list[:idx] + my_list[idx+1:] if 0 <= idx < len(my_list) else my_list
