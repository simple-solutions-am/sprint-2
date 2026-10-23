digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(digits[0],digits[-1])
print(digits[5],digits[-4])
print(digits[2:6])
print(digits[::2])
print(digits[::-1])
print(digits.count(1), digits.count(5))
print(min(digits),max(digits),sum(digits))
print(digits.index(5))
backup = digits.copy()
reversed_digits = backup[::-1]
print(len(digits) - 1 - backup[::-1].index(5))

fives = []
for i, num in enumerate(digits):
    if num == 5:
        fives.append(i)
print(fives)

try:
    print(digits.index(7))
except ValueError:
    print('7 не найдено')

for i, five in enumerate(backup):
    if five == 5:
        backup[i] = 0
print(backup)
