import time
import conversor

opt = 0

print("Escolha a Escala para Conversão")
time.sleep(1)

while opt != 7:
    print("1 - Fahrenheit para Celsius\n2 - Fahrenheit para Kelvin\n3 - Kelvin para Celsius")
    opt = int(input("4 - Kelvin para Fahrenheit\n5 - Celsius para Fahrenheit\n6 - Celsius para Kelvin\n7 - Sair\n"))
    if opt == 1:
        conversor.FtoC()
        time.sleep(1)
    if opt == 2:
        conversor.FtoK()
        time.sleep(1)
    if opt == 3:
        conversor.KtoC()
        time.sleep(1)
    if opt == 4:
        conversor.KtoF()
        time.sleep(1)
    if opt == 5:
        conversor.CtoF()
        time.sleep(1)
    if opt == 6:
        conversor.CtoK()
        time.sleep(1)
    if opt == 7:
        print("Programa Encerrando ...")