try:
    var_1 = False
    while not var_1:
        var_1 = input("Please type a number:")
        if not var_1.isnumeric():
            var_1 = False
            print("Only digits, please. NO SPACE\n Example:123")
        else:
            break
    var_2 = False
    while not var_2:
        var_2 = input("Second number:")
        if not var_2.isnumeric():
            var_2 = False
            print("Only digits, please. NO SPACE\n Example:123")
        else:
            break

    var_3 = False
    while not var_3:
        var_3 = input("Choose operation: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'")
        if var_3 == "1":
            result = float(var_1) + float(var_2)
            print("Result: ")
            print(result)
        elif var_3 == "2":
            result = float(var_1) - float(var_2)
            print("Result: ")
            print(result)
        elif var_3 == "3":
            result = int(var_1) * float(var_2)
            print("Result: ")
            print(result)
        elif var_3 == "4":
            result = float(var_1) / float(var_2)
            print("Result: ")
            print(result)

        else:
            if not var_3 == "1" or not var_3 == "2" or not var_3 == "3" or not var_3 == "4":
                print("Operators should be chosen 1 or 2 or 3 or 4.\nOnly digits, NO SPACE\n")
        ######!!!! ТУТ ДАЛЬШЕ НЕ ЗНАЮ КАК ВЕРНУТЬ К var_3 !!!!!
            break

except ZeroDivisionError:
    print("Can't be divided on 0")
except ValueError:
    print("Sorry, server out of order now")
