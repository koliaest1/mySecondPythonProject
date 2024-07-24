deposit = int(input())
years = 0
LIM = 700000
INTEREST = 0.071
while deposit < LIM:
    years += 1
    deposit = deposit + deposit * INTEREST
print(years)
