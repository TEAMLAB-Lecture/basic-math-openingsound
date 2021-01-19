#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):

    greatest_number = number_list[0]
    for number in number_list:
        if number > greatest_number:
            greatest_number = number
    return greatest_number


def get_smallest(number_list):

    smallest_number = number_list[0]
    for number in number_list:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


def get_mean(number_list):

    mean = 0
    for number in number_list:
        mean += number
    mean = mean / number_list.size()
    return mean


def get_median(number_list):
    number_list.sort()
    median = None
    point = number_list.size()//2 # 중간지점
    if(number_list.size()%2):
        median = number_list[point]
    else:
        median = (number_list[point-1] + number_list[point])/2

    return median
