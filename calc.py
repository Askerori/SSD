

def slo():
    x = int(input("Введите первое число:"))
    y = int(input("Введите второе число:"))
    z = x + y
    print("Ответ:",z)

def min():
    x = int(input("Введите первое число:"))
    y = int(input("Введите второе число:"))
    z = x - y
    print("Ответ:",z)

    def ymn():
        x = int(input("Введите первое число:"))
        y = int(input("Введите второе число:"))
        z = x * y
        print("Ответ:",z)

    def delen():
        x = int(input("Введите первое число:"))
        y = int(input("Введите второе число:"))
        z = x / y
        print("Ответ:",z)

    r = input("Какое действие хотите произвести(+,-,*,/)")
    if r == "+":
        slo()
    elif r == "-":
        min()
    elif r == "*":
        ymn()
    elif r == "/":
        delen()  
    else:
        print("Error")
          

