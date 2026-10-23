def formatir(n1, n2, n3, n4):
    end = f"{n1:02d}, {n2:02d}, {n3:02d}, {n4:02d}"
    return end

result = formatir(7,74,743,7438)
print(result)

zap = 1499.5
print(f'{zap:.2f}')

number = 1234567.891
print(f"{number:,.2f}")

number1 = 1234567.891
print(f"{number1:,.2f}".replace(","," "))

proc = 875
print(f'f"{proc:.1%}')

day = 5
month = 3
year = 2026
print(f'{day:02d}.{month:02d}.{year}')

word = "Чек"
print(f'{word:*^20}')

cart = [("Хлеб", 45), ("Молоко", 89), ("Чокопай", 120)]

print(f'{cart[0][0]:<10}{cart[0][1]:>6} руб.')
print(f'{cart[1][0]:<10}{cart[1][1]:>6} руб.')
print(f'{cart[2][0]:<10}{cart[2][1]:>6} руб.')
total = cart[0][1] +cart[1][1] +cart[2][1]

print(f"{'Итого':<10}{total:>6} руб.")
