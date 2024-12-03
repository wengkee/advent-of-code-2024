from data_file import DataFile
import re

data_file = DataFile("data/d3.data")
total, total2 = 0, 0
toProcess = True
def find_and_evaluate_multiplications(input_string):

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_string)

    pattern2 = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
    matches2 = re.finditer(pattern2, input_string)

    for match in matches:
        global total
        total += int(match[0]) * int(match[1])
    
    for match2 in matches2:
        global toProcess
        if match2.group(0) == "do()":
            toProcess = True
        elif match2.group(0) == "don't()":
            toProcess = False
        elif toProcess:
            num1, num2 = map(int, match2.groups()[1:3])
            global total2
            total2 += num1*num2

        


for line in data_file.lines:
    find_and_evaluate_multiplications(line)
print(total)
print(total2)