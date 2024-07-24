count = 0
summary = 0
while True:
    number = int(input())
    summary += number
    count += 1
    if number == 55:
        average = round(summary / count)
        print(count)
        print(summary)
        print(average)
        break