print("Welcome to treasure island")

stage1 = input("Left or right:")

if stage1.lower() == "right":
    print("Game Over")
elif stage1.lower() == "left":
    stage2 = input("Swim or wait: ")
    if stage2.lower() == "swim":
        print("Game Over")
    elif stage2.lower() == "wait":
        stage3 = input("Which door. Red, Yellow or Blue ")
        if stage3.lower() == "red" or stage3.lower() == "blue":
            print("Game Over")
        elif stage3.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over")