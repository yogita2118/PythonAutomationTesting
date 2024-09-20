with open("TestData.txt", "r") as file:
    lines = file.readline()
    for line in lines:
        print(line,end="")
