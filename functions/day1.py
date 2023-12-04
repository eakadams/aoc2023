# Day1 : Trebuchet calibration

import regex as re

def read_input(textfile):
    """
    Read each input line into a string
    :param textfile:
    :return:
    """
    with open(textfile, 'r', encoding="utf-8") as f:
        input_lines = f.readlines()
    return input_lines


def find_numerals(string_list):
    """
    Find numerals for each line in a string list
    :param string_list:
    :return:
    """
    numeral_list = []
    for line in string_list:
        numeral_list.append(re.findall('\d', line))

    return numeral_list


def find_numerals_spelled(string_list):
    """
    Find numerals for each line when they can also be spelled out
    :param string_list:
    :return:
    """
    # set up pattern for matching
    pattern = '\d|one|two|three|four|five|six|seven|eight|nine'
    # print(pattern)
    numeral_list = []
    for line in string_list:
        temp = re.findall(pattern, line, overlapped=True)
        print(line, temp)
        #print(temp)
        numeral_list.append(temp)

    return numeral_list

def get_calibration_values(numeral_list):
    """
    Get calibration value as first and last numeral for each line
    :param numeral_list:
    :return:
    """
    calibration_list = []
    for line in numeral_list:
        cal_string = line[0]+line[-1]
        calibration_list.append( int(cal_string) )

    return calibration_list

def get_calibration_values_spelled(numeral_list):
    """
    Get calibration value as first and last numeral for each line
    If spelled out, return number
    :param numeral_list:
    :return:
    """
    dict_values = {'one': '1', 'two': '2', "three":'3', 'four':'4', 'five':'5',
                   'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    calibration_list = []
    for line in numeral_list:
        if len(line[0]) > 1:
            line0 = dict_values[line[0]]
        else:
            line0 = line[0]
        if len(line[-1]) > 1:
            line1 = dict_values[line[-1]]
        else:
            line1 = line[-1]
        cal_string = line0 + line1
        #print(line, cal_string)
        calibration_list.append(int(cal_string))

    return calibration_list


def get_sum_calibration_values(input_file):
    input_lines = read_input(input_file)
    numeral_list = find_numerals(input_lines)
    calibration_value_list = get_calibration_values(numeral_list)
    sum_calibration_vals = sum(calibration_value_list)

    return sum_calibration_vals

def get_sum_cal_values_spelled(input_file):
    input_lines = read_input(input_file)
    numeral_list = find_numerals_spelled(input_lines)
    calibration_value_list = get_calibration_values_spelled(numeral_list)
    sum_cal_values = sum(calibration_value_list)

    return sum_cal_values