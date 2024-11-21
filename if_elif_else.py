num1 = input("Введите число: ")
num2 = input("Введите второе число: ")
num3 = input("Введите третье число: ")
if num1 == num2 == num3:
    print(3)
if num1 == num2 or num2 == num3 or num3 == num1:
    print(2)
else:
    print(0)   
