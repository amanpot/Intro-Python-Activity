numItems = int(input("Number of items:"))

list = dict()

for i in range(numItems):
    listInput = input(("Input item and price:"))
    temp = listInput.split(' ')
    list[temp[0]] = int(temp[1])

    listSort = sorted(list.items(), key=lambda x:x[1], reverse=False)

    for i in listSort:
        print(i[0], i[1])
    