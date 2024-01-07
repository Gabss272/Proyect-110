import random

while True:
    print("¿Quieres tirar un dado?")
    ask = input("1 = Si, 2 = No: ")

    if ask == "1":
        num = random.randint(1, 6)
        if num == 1:
            print("-------")
            print("       ")
            print("   0   ")
            print("       ")
            print("-------")
        elif num == 2:
            print("-------")
            print("     0 ")
            print("       ")
            print("  0    ")
            print("-------")
        elif num == 3:
            print("-------")
            print("    0  ")
            print("   0   ")
            print("  0    ")
            print("-------")
        elif num == 4:
            print("-------")
            print(" 0   0 ")
            print("       ")
            print(" 0   0 ")
            print("-------")
        elif num == 5:
            print("-------")
            print(" 0   0 ")
            print("   0    ")
            print(" 0   0 ")
            print("-------")
        else:
            print("-------")
            print(" 0   0 ")
            print(" 0   0 ")
            print(" 0   0 ")
            print("-------")

        ask = input("¿Quieres tirar el dado otra vez? (1/2): ")
    elif ask == "2":
        print("¡Gracias por jugar! Hasta luego.")
        break
    else:
        print("Respuesta no válida. Por favor, ingresa '1' o '2'.")