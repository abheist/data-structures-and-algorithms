

# open file,
# read file until next blank line
# sum every value until blank line and add it to list
# once every line is done, return the max

def calorie_counting():
    calories = []
    file = open('advent-of-code/input.txt', 'r')
    lines = file.readlines()
    person_calories = 0
    for line in lines:
        if line == "\n":
            calories.append(person_calories)
            person_calories = 0
            continue
        person_calories += int(line)
    return calories


calories = calorie_counting()

max_three_calories = sorted(calories)[-3:]

print(sum(max_three_calories))
