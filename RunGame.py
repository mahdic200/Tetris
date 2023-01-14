isTrue = True
while isTrue:
    print("which one do you want ?")
    print("Standard --> 1")
    print("Project  --> 0")
    userInput = int(input())

    if userInput == 1:
        isTrue = False
        import Standard.Standard_Tetris as Standard_Tetris
    elif userInput == 0:
        isTrue = False
        import project.main as main
    else:
        print("*******\n")
        print("input is not valid !\n")
        print("*******\n")
