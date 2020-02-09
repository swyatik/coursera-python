# перевірка вводу вихідних даних
while True:
    n = input("Height: ") # півдіагональ ромба
    if n.isdigit():
        if int(n) > 0:
                break
x = int(n)*2 - 1 #rhomb height and length

# друк
for i in range(x):
    space_number = 0  # кількість перших надрукованих пробілів

    if i < int(n):
        if i > 0:
            for j in range(int(n) - i - 1):
                print(" ", end="")
                space_number += 1

            print("#", end="")

            for h in range(x - (space_number * 2 + 2)):
                print(" ", end="")
            print("#", end="")
            print()

    if i >= int(n):
        if i < x - 1:
            for j in range(i - int(n) + 1):
                print(" ", end="")
                space_number += 1

            print("#", end="")

            for h in range(x - (space_number * 2 + 2)):
                    print(" ", end="")
            print("#", end="")
            print()