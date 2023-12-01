pairs = []

digits = {  
        1: "one",
        2: "two",
        3: "three",
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine"
    }

total = 0
with open("./input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        first = ""
        last = ""
        pair = []
        for key, char in enumerate(line):
            if char.isdigit():
                pair.append(char)
            for indice, number in digits.items():
                if line.startswith(number, key):
                    pair.append(str(indice))
        total = total + int(pair[0] + pair[-1])

print(total)
