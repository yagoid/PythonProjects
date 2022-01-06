import random
import os

# Lucha de pokemon

Vida_picachu = 0
Vida_squirtle = 0

while Vida_picachu < 20 or Vida_picachu > 200 or Vida_squirtle < 20 or Vida_squirtle > 200:
    Vida_picachu = int(input("Elije la vida de Pikachu [20 - 200]\n"))
    Vida_squirtle = int(input("Elige la vida de Squirtle [20 - 200]\n"))

Vida_total_pikachu = int(Vida_picachu)
Vida_total_squirtle = int(Vida_squirtle)

while Vida_picachu > 0 and Vida_squirtle > 0:

    # Turno de Pikachu
    print("\nTurno de ataque de Pikachu")
    print("Ataques:\n[rayo voltio = 10 vida]\n[onda trueno = 15 vida]")

    Ataque_pikachu = int(random.randint(1,2))

    # Si ataque_pikachu es 1, se hace ataque rayo voltio y si es 2, onda trueno
    if Ataque_pikachu == 1:
        Vida_squirtle -= 10
        porcentaje_vida = int((100 * (Vida_squirtle/Vida_total_pikachu))/10)
        porcentaje_vida_restante = int(10 - porcentaje_vida)

        print("Pikachu usa el ataque RAYO VOLTIO.\n Vida de Squirtle: ",
              '[' + '#'*porcentaje_vida + '-'*porcentaje_vida_restante + ']', "({}/{})".format(Vida_squirtle, Vida_total_squirtle))
    else:
        Vida_squirtle -= 15
        porcentaje_vida = int((100 * (Vida_squirtle/Vida_total_pikachu))/10)
        porcentaje_vida_restante = int(10 - porcentaje_vida)

        print("Pikachu usa el ataque ONDA TRUENO.\n Vida de Squirtle: ",
              '[' + '#'*porcentaje_vida + '-'*porcentaje_vida_restante + ']', "({}/{})".format(Vida_squirtle, Vida_total_squirtle))


    # Turno de Squirtle
    print("\n\nTurno de ataque de Squirtle")
    input("Presiona Enter para continuar\n")

    Ataque_squirtle = ""

    while Ataque_squirtle != "A" and Ataque_squirtle != "B" and Ataque_squirtle != "C":
        Ataque_squirtle = str(input("Elije ataque:\nA - [Placaje = -10 vida]\nB - [Pistola agua = -12 vida]\nC - [Burbuja = -9 vida]\n"))
        Ataque_squirtle.upper()

    if Ataque_squirtle == "A":
        Vida_picachu -= 10
        porcentaje_vida = int((100 * (Vida_picachu / Vida_total_pikachu)) / 10)
        porcentaje_vida_restante = int(10 - porcentaje_vida)

        print("Squirtle usa el ataque PLACAJE.\n Vida de Picachu: ",
              '[' + '#'*porcentaje_vida + '-'*porcentaje_vida_restante + ']', "({}/{})".format(Vida_picachu, Vida_total_pikachu))

    elif Ataque_squirtle == "B":
        Vida_picachu -= 12
        porcentaje_vida = int((100 * (Vida_picachu / Vida_total_pikachu)) / 10)
        porcentaje_vida_restante = int(10 - porcentaje_vida)

        print("Squirtle usa el ataque PISTOLA AGUA.\n Vida de Picachu: ",
              '[' + '#'*porcentaje_vida + '-'*porcentaje_vida_restante + ']', "({}/{})".format(Vida_picachu, Vida_total_pikachu))

    elif Ataque_squirtle == "C":
        Vida_picachu -= 9
        porcentaje_vida = int((100 * (Vida_picachu / Vida_total_pikachu)) / 10)
        porcentaje_vida_restante = int(10 - porcentaje_vida)

        print("Squirtle usa el ataque BURBUJA.\n Vida de Picachu: ",
              '[' + '#'*porcentaje_vida + '-'*porcentaje_vida_restante + ']', "({}/{})".format(Vida_picachu, Vida_total_pikachu))

    input("Presiona Enter para continuar\n")
    os.system("cls")


if Vida_picachu < Vida_squirtle:
    print("\n\nHa ganado Squirtle. Felicidades Squirtle!!")
else:
    print("\n\nHa ganado Pikachu. Felicidades Pikachu!!")
