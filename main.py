number1 = int(input("Введіть перше число:"))
number2 = int(input("Введіть друге число:"))
number3 = int(input("Введіть третє число:"))
# Ми тимчасово припускаємо, що перше число найбільше.
# Ми скоро це перевіримо.
largest_number = number1
# Ми перевіряємо чи більше друге число, ніж поточне largest_number та оновлюємо largest_number за необхідності
if number2 > largest_number:
   largest_number = number2
# ми перевіряємо чи більше третє числоб ніж поточне Largest_number та оновлюємо largest_number за необхідності
if number3 > largest_number:
   largest_number = number3
# Вивід результату
print("Ваше найбільше число :", largest_number)
