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
    mean = mean / len(number_list)
    return mean


def get_median(number_list):
    number_list.sort()
    median = None
    point = len(number_list)//2 # 중간지점
    if(len(number_list)%2):
        median = number_list[point]
    else:
        median = (number_list[point-1] + number_list[point])/2

    return median

"""def main():
    print("******get_greatest******")
    print(96==get_greatest([95, 61, 96, 45, 27, 86, 33, 66, 4, 39]))
    print( 87 == get_greatest([19, 35, 4, 21, 29, 87, 32, 10, 53, 63]))
    print('\n')

    print("******get_smallest******")
    print(5==get_smallest([75, 40, 5, 45, 14, 17, 35, 37, 57, 21]))
    print( 20 == get_smallest([83, 89, 36, 20, 70, 75, 44, 56, 21, 77]))
    print('\n')

    print("******get_mean******")
    print(56.5==get_mean([55, 93, 22, 67, 98, 11, 5, 68, 57, 89]))
    print( 51.4 == get_mean( [7, 67, 6, 53, 62, 93, 56, 81, 9, 80]))
    print('\n')

    print("******get_median******")
    print(55.0==get_median([6, 75, 79, 41, 38, 77, 1, 30, 69, 83]))
    print( 36 == get_median([6, 93, 23, 7, 3, 99, 36, 51, 70, 89, 5]))
    print('\n')

if __name__ =="__main__":
    main()"""