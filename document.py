maxLenght = 0
number = 0
for i in range(1, 1000000):
    currentNumber = i
    lenght = 1
    while currentNumber != 1:
        if currentNumber % 2 == 0:
            currentNumber /= 2
        else: 
            currentNumber = 3 * currentNumber + 1
        lenght = lenght + 1
    if lenght > maxLenght:
        maxLenght = lenght
        number = i
print(number)