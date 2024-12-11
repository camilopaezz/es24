import math

input = "10 9 12 5 3 4 8 10 11 10 9 8"
# input = "1 2 3 4"

n_list = input.split()
n_list = list(map(int, n_list))

calc = None

def thanos_sort(list: list):
    is_sorted = True
    global calc

    if len(list) == 1:
        return list

    for i in range(1, len(list)):
        if list[i - 1] < list[i]:
            continue
        else:
            is_sorted = False
            break

    if is_sorted:
        calc = len(list)
    # else:
    #     middle = math.floor(len(list) / 2)
    #     print(middle)
        
    #     a_side = thanos_sort(list[:middle + 1])
    #     b_side = thanos_sort(list[middle+1:])
        

thanos_sort(n_list)
# print(calc)
