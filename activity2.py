def checker(firstNum, secondNum):
    num = firstNum
    for num in range(firstNum, secondNum):
        if num % 7 == 0:
            if num % 5 != 0:
                print(num)  # print must be inside the condition
        num += 1  # the increase must be done on every iteration
    

firstNum = input("Enter your first number:")
secondNum = input("Enter your second number:")

firstNum = int(firstNum)
secondNum = int(secondNum)

stringToReturn = checker(firstNum, secondNum)
print(stringToReturn)

