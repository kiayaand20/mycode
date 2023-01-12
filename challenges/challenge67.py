#!usr/bin/env python3

count = 0

with open("dracula.txt", "r") as vampire:
    with open("vampytimes.txt", "w") as fangs:
        for lines in vampire:
            if "vampire" in lines.lower(): 
                print(lines)
                count += 1
                fangs.write(lines)

print(count)
