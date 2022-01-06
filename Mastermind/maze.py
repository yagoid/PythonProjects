import random
import os
import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 10

my_position = [3, 0]
tail_length = 0
tail = []
map_objects = []

end_game = False

# Generamos objetos alatorios en el mapa
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    xy_random = [int(random.randint(0, MAP_WIDTH-1)), int(random.randint(0, MAP_HEIGHT-1))]

    if xy_random not in map_objects and xy_random != my_position:
        map_objects.append(xy_random)

while not end_game:
    # Dibujar mapa
    print("+" + "-" * MAP_WIDTH*3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            # Se dibuja la cola del snake
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            # Se dibuja la cabeza del snake
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = "@"

                if my_position in tail:
                    print("Has muerto!")
                    end_game = True

            # Se dibujan los objetos en el mapa
            for map_object in map_objects:
                if my_position[POS_X] == map_object[POS_X] and my_position[POS_Y] == map_object[POS_Y]:
                    map_objects.remove(map_object)
                    tail_length += 1

                if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]:
                    char_to_draw = "*"

            print(" " + char_to_draw + " ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH*3 + "+")

    # Preguntar al usuario donde se quiere mover
    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH

    elif direction == "e":
        end_game = True

    os.system("cls")