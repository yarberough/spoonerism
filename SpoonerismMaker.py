while True:
    print("Make a Spoonerism")
    print(" ")
    fword = str(input("Enter the first word: "))
    sword = str(input("Enter the second word: "))
    if fword[:2] == "qu" or fword[1] == "b" or fword[1] == "c" or fword[1] == "d" or fword[1] == "f" or fword[1] == "g" or fword[1] == "h"  or fword[1] == "j" or fword[1] == "k" or fword[1] == "l" or fword[1] == "m" or fword[1] == "n" or fword[1] == "p" or fword[1] == "q" or fword[1] == "r" or fword[1] == "s" or fword[1] == "t" or fword[1] == "v" or fword[1] == "w" or fword[1] == "x" or fword[1] == "y" or fword[1] == "z":
        if sword[:2] == "qu" or sword[1] == "b" or sword[1] == "c" or sword[1] == "d" or sword[1] == "f" or sword[1] == "g" or sword[1] == "h" or sword[1] == "j" or sword[1] == "k" or sword[1] == "l" or sword[1] == "m" or sword[1] == "n" or sword[1] == "p" or sword[1] == "q" or sword[1] == "r" or sword[1] == "s" or sword[1] == "t" or sword[1] == "v" or sword[1] == "w" or sword[1] == "x" or sword[1] == "y" or sword[1] == "z":
            print(" ")
            print(sword[:2] + fword[2:] + " " + fword[:2] + sword[2:])
            print(" ")
            input("Press enter to make another: ")
            import os, platform
            def clear():
                if platform.system() == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear')
            clear()
        else:
            print(" ")
            print(sword[0] + fword[2:] + " " + fword[:2] + sword[1:])
            print(" ")
            input("Press enter to make another: ")
            import os, platform
            def clear():
                if platform.system() == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear')
            clear()
    else:
        if sword[:2] == "qu" or sword[1]  == "b" or sword[1] == "c" or sword[1] == "d" or sword[1] == "f" or sword[1] == "g" or sword[1] == "h" or sword[1] == "j" or sword[1] == "k" or sword[1] == "l" or sword[1] == "m" or sword[1] == "n" or sword[1] == "p" or sword[1] == "q" or sword[1] == "r" or sword[1] == "s" or sword[1] == "t" or sword[1] == "v" or sword[1] == "w" or sword[1] == "x" or sword[1] == "y" or sword[1] == "z":
            if fword[:2] == "qu" or fword[1] == "b" or fword[1] == "c" or fword[1] == "d" or fword[1] == "f" or fword[1] == "g" or fword[1] == "h" or fword[1] == "j" or fword[1] == "k" or fword[1] == "l" or fword[1] == "m" or fword[1] == "n" or fword[1] == "p" or fword[1] == "q" or fword[1] == "r" or fword[1] == "s" or fword[1] == "t" or fword[1] == "v" or fword[1] == "w" or fword[1] == "x" or fword[1] == "y" or fword[1] == "z":
                print(" ")
                print(sword[:2] + fword[2:] + " " + fword[:2] + sword[2:])
                print(" ")
                input("Press enter to make another: ")
                import os, platform
                def clear():
                    if platform.system() == 'Windows':
                        os.system('cls')
                    else:
                        os.system('clear')
                clear()
            else:
                print(" ")
                print(sword[:2] + fword[1:] + " " + fword[0] + sword[2:])
                print(" ")
                input("Press enter to make another: ")
                import os, platform
                def clear():
                    if platform.system() == 'Windows':
                        os.system('cls')
                    else:
                        os.system('clear')
                clear()
        else:
            print(" ")
            print(sword[0] + fword[1:] + " " + fword[0] + sword[1:])
            print(" ")
            input("Press enter to make another: ")
            import os, platform
            def clear():
                if platform.system() == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear')
            clear()