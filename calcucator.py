try:
  var_1 = input("Please type a number:")
# it_true = True
  while var_1.isnumeric() is not True:
   print("Only digits, please\n Example:123")
   break

# Коля, крутила и не все равно поняла, как остановить и вернуть пользователя к var_1 & var_2, соответственно.
# Сорри.
# Мастер , подскажи :)


  var_2 = input("Please type another number:")
  while var_2.isnumeric() is not True:
      print("Only digits, please\n Example:123")
      break

  var_3 = input("Choose operation: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'")
  if var_3 == "1":
    result = float(var_1) + float(var_2)
    print("Result: ")
    print(result)
  if var_3 == "2":
    result = float(var_1) - float(var_2)
    print("Result: ")
    print(result)
  if var_3 == "3":
     result = int(var_1) * float(var_2)
     print("Result: ")
     print(result)
  if var_3 == "4":
    result = float(var_1) / float(var_2)
    print("Result: ")
    print(result)
    ## 0,word,type,minus, empty row #### if except --------- пустота
except ZeroDivisionError:
      print("Can't be divided on 0")
except ValueError:
  print("Sorry, server out of order now")
