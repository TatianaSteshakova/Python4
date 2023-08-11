num = float(input("Введите пятизначное число: "))

ten_thousands = num // 10000
thousands = (num // 1000) % 10
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10

res = (pow(tens, units) * hundreds) / (ten_thousands - thousands)

print(res)