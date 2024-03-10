from random import randint

print("NUMBER GUESS")

number = randint(1, 10)

while True:
    answer = int(input("whats the number my friend? "))

    if answer == number:
        print("yayayayayayyayayayyayayayayayayaayya")
        break

    else:
        print("you blithering idiot")
