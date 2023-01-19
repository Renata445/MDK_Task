n = int(input("Введите число n: "))
hours = n % (60 * 24) // 60
minutes = n % 60
print(str(hours) + ":" + str(minutes))