import json


def check_lists(xn_list):
    if len(xn_list) == len(set(xn_list)):
        return True
    else:
        return False


variables = open("output.txt", "r")
count = 0
for line in variables:
    line = json.loads(line.replace("'", '"'))
    list_txt = line['list']
    if check_lists(list_txt):
        print(len(list_txt), line['m'], count)
        count += 1
variables.close()
