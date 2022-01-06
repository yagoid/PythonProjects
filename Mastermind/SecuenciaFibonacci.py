

def secuencia_fibonacci(nums_objetivo):

    nums_fibonacci = [0, 1]

    if nums_objetivo:
        for a in range(nums_objetivo):
            largo = len(nums_fibonacci)-1

            numero = (nums_fibonacci[largo])+(nums_fibonacci[largo-1])
            nums_fibonacci.append(numero)

            print(nums_fibonacci[a])


def main():
    secuencia_fibonacci(22)


if __name__ == "__main__":
    main()