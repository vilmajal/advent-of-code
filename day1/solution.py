import re

with open("input.in") as f:
    data = f.read().strip()

    def calibration(data):
        answer = 0
        data = data.split("\n")
        for line in data:
            number = re.findall("\d", line)
            new_number = number[0]+number[-1]
            answer += int(new_number)
        return answer

#Part 1
    print("part1", calibration(data))

#part 2
    data = (
        data.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )
    print("part2", calibration(data))

