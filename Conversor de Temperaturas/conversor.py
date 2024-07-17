def FtoC():
    temp = int(input("Digite a Temperatura em Fahrenheit: "))
    print("A temperatura em Celsius é:", round((temp-32) * (5/9), 2))
def FtoK():
    temp = int(input("Digite a Temperatura em Fahrenheit: "))
    print("A Temperatura em Kelvin é:", round((temp - 32) * (5 / 9) + 273.15, 2))
def KtoC():
    temp = int(input("Digite a Temperatura em Kelvin: "))
    print("A Temperatura em Celsius é:", round(temp-273.15,2))
def KtoF():
    temp = int(input("Digite a Temperatura em Kelvin: "))
    print("A Temperatura em Fahrenheit é:", round((temp-273.15)*9/5+32, 2))
def CtoF():
    temp = int(input("Digite a Temperatura em Celsius: "))
    print("A Temperatura em Fahrenheit é:", round(temp*9/5+32,2))
def CtoK():
    temp = int(input("Digite a Temperatura em Celsius: "))
    print("A Temperatura em Kelvin é:", temp+273.15)