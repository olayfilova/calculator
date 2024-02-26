# while True:
#     try:
#         var_1 = False
#         while not var_1:
#             var_1 = input("Please type a number:")
#             if not var_1.isnumeric():
#                 var_1 = False
#                 print("Only digits, please. NO SPACE\n Example:123")
#             else:
#                 break
#         var_2 = False
#         while not var_2:
#             var_2 = input("Second number:")
#             if not var_2.isnumeric():
#                 var_2 = False
#                 print("Only digits, please. NO SPACE\n Example:123")
#             else:
#                 break
#
#         var_3 = False
#         while not var_3:
#             var_3 = input("Choose operation: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'")
#             if var_3 == "1":
#                 result = float(var_1) + float(var_2)
#                 print("Result: ")
#                 print(result)
#             elif var_3 == "2":
#                 result = float(var_1) - float(var_2)
#                 print("Result: ")
#                 print(result)
#             elif var_3 == "3":
#                 result = float(var_1) * float(var_2)
#                 print("Result: ")
#                 print(result)
#             elif var_3 == "4":
#                 result = float(var_1) / float(var_2)
#                 print("Result: ")
#                 print(result)
#
#             else:
#                 if not var_3 == False:
#                     print("Operators should be chosen 1 or 2 or 3 or 4.\nOnly digits, NO SPACE\n")
#                 break
#             print("would you like to proceed?")
#
#     except ZeroDivisionError:
#         print("Can't be divided on 0")
#     except ValueError:
#         print("Sorry, server out of order now")
#
#     continue

# val_1 = 10
# print(val_1/2) if int(val_1)<100 else print(f"-{val_1}")
# print(1) if val_1 < 100 else print(0)
# print(int(True)) if val_1 < 100 else print(int(False))
# print(True) if val_1 < 100 else print(False)

# str = "abcderrrr"
# print((str) * 2) if len(str) <= 5 else print(str)
# print(str + str[::-1]) if len(str) <= 5 else print(str)

# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.

# num = 100100
# val_res = str(num)
# res = val_res.count("0")
# print(res)

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# num = 102000
# num_str = str(num)
# zro = 0
#
# for i in num_str[::-1]:
#     if i == "0":
#         zro += 1
#     else:
#         break
# print(zro)

# 3 Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_lst_1 = ["13", "i no", "3", "4"]
# my_lst_2 = ["10", "20", "30", "40"]
# my_res =[]
#
# my_res = my_lst_1[::2].__add__(my_lst_2[1::2])
# print(my_res)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]
#
# my_list = [1,2,3,4]
# new_list = []
# res = my_list[1::].__add__(my_list[:1])
# print(res)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
# my_list = [1, 2, 3, 4]
# first_pop = my_list.pop(0)
# my_list.append(first_pop)
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# val = "43 більше ніж 34, але менше ніж 56"
# digit_list = []
# val_replace = val.replace(",", " ")
# # print(val_replace)
# val_replace = val_replace.split(" ")
# # print(val_replace)
#
# for i in val_replace:
#     if i.isdigit():
#         digit_list.append(i)
# # print(digit_list)
# total = 0
# for num in digit_list:
#     total += int(num)
# # res = sum(digit_list)
# print(total)

# # 6.2
# val = "43 більше ніж 34, але менше ніж 56"
# new_list = []
#
# for i in val:
#     if not i.isdigit():
#         val=val.replace(i, " ")
#
# new_list =val.split()
# total = 0
# # print(new_list)
# for num in new_list:
#     total+= int(num)
# print(total)

# 6.3

# val = "43 is grater than 34, but less than 56"
# new_list = []
#
# for word in val.split():
#     if word.isdigit():
#         new_list.append(int(word))
#         # print(new_list)
#     else:
#         dig = ""
#         for smbl in word:
#             if smbl.isdigit():
#                 dig+=smbl
#
#             else:
#                 if dig:
#                     new_list.append((int(dig)))
#                     dig =""
#
# res = sum(new_list)
# print(res)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# val_1 = [2, 1, 1, 5, 3, 9, 0, 7]
# count = 0
# for i in range(1, len(val_1) - 1):
#     if val_1[i] > val_1[i + 1] + val_1[i - 1]:
#         count += 1
#
# print(count)

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", '22', 33]
# new_list = []
# for i in my_list:
#     if type(i) is str:
#         new_list.append(i)
# print(new_list)

# 9 Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = "abcabcABCa,,.fgjf"
# new_list = []
# count = 0
#
# for i in my_str:
#     a = my_str.count(i)
#     if a == 1:
#         new_list.append(i)
# print(new_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# str_1 = "abcdevv112"
# str_2 = "ade2"
# new_list = []
#
# str_1_set = set(str_1)
# str_2_set = set(str_2)
# res = list(str_1_set.intersection(str_2_set))
# new_list.extend(sorted(res))
# print(new_list)
#
#
# str_1 = "abcdevv112"
# str_2 = "ade2"
# new_list = []
#
# for i in str_1 and str_2:
#     if i in str_1 and str_2:
#         new_list.append(i)
# print(new_list)
#
# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу
#
# str_1 = "aaaasdf1"
# str_2 = "asdfff2"
# new_list = []
# count = 0
# for i in str_1 and str_2:
#     if i in str_1 and str_2 and str_1.count(i) == 1 and str_2.count(i) == 1:
#         new_list.append(i)
# print(new_list)

# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.
# my_list = ["abc", "123", "4", "12", 'dce', 'fjh']
# new_list = []
# print(new_list)
#
# for j, k in enumerate(my_list):
#     if j % 2 == 1:
#         new_list.append(k[::-1])
#     else:
#         new_list.append(k)
# print(new_list)
#
# for j, k in enumerate(my_list):
#     if j % 2 == 1:
#         rev_str = k[::-1]
#         new_list.append(rev_str)
#     else:
#         new_list.append(k)
# print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

# my_list = ["abc", "bca", "adv", "dva"]
# new_list = [i for i in my_list if i.startswith("a")]
# print(new_list)
#
#
# my_list = ["abc", "bca", "adv", "dva"]
# new_list = [i for i in my_list if i[0] == "a"]
# print(new_list)
#
#
# my_list = ["abc", "bca", "adv", "dva"]
# for i in my_list:
#     if i.startswith("a"):
#         new_list.append(i)
# print(new_list)
#
#
# my_list = ["abc", "bca", "adv", "dva"]
# for i in my_list:
#     if i[0] == "a":
#         new_list.append(i)
# print(new_list)


# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

my_list = ["hjk", "abc", "bca", "adv", "dva"]
new_list = []

for i in my_list:
    if "a" in i:
        new_list.append(i)
print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# в) Порахувати середню вік усіх людей із початкового списку.


# 5) Дано два словники my_dict_1 і my_dict_2.
# а) Створити список із ключів, які є в обох словниках.
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict = {"key": "value",
           "addres": "Dublin",
           "city": "Dublin",
           }

for i in my_dict:
    print(i)

for i, k in enumerate(my_dict):
    print(i, k)

for i in my_dict.items():
    print(i)

print(my_dict.keys())
print(my_dict.values())

person = dict()

person["name"] = "Daniel"
person["age"] = "21"

print(person)


person_1 = dict()

person_1["name"] = "John"
person_1["age"] = "21"

print(person_1)


person_2 = dict()

person_2["name"] = "Kelvin"
person_2["age"] = "21"

print(person_2)

print(person_2.get("age", False))
print(person_2.get("email", False))


checkin
if "city" not in person_2:
    print("You have to type your city.")


from random import randint

res = randint(1, 5)

dict_1 = {1: "5",
        2: "6",
        3: "7",
        4: "8",
        5: "9",
        }

print(dict_1[res])

alf_dict ={}

# alf_dict[chr()]= "97"
# print(alf_dict)

for key in range(ord("a"), ord("z")+1):
        print(key)


alfa_dict = {}

for i in range(ord("a"), ord("z")):
    alfa_dict[i] = chr(i)

print(alfa_dict)

alfa_dict_2 = {}

for i in alfa_dict:
    alfa_dict_2[alfa_dict[i]] = i
print(alfa_dict_2)

for i, k in alfa_dict.items():
    alfa_dict_2[k] = i
print(alfa_dict_2)
