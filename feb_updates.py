val_1 = 10
print(val_1/2) if int(val_1)<100 else print(f"-{val_1}")
# print(1) if val_1 < 100 else print(0)
# print(int(True)) if val_1 < 100 else print(int(False))
# print(True) if val_1 < 100 else print(False)

# str = "the Australian and New Zealand Standard Classification of Occupations (ANZSCO) code for each occupation."
# print((str) * 2) if len(str) <= 5 else print(str)
# print(str + str[::-1]) if len(str) <= 5 else print(str)

num = 100100
val_res = str(num)
res = val_res.count("0")
print(res)

num = 102000
num_str = str(num)
zro = 0

for i in num_str[::-1]:
    if i == "0":
        zro += 1
    else:
        break
print(zro)


my_lst_1 = ["13", "i no", "3", "4"]
my_lst_2 = ["10", "20", "30", "40"]
my_res =[]

my_res = my_lst_1[::2].__add__(my_lst_2[1::2])
print(my_res)

my_list = [1,2,3,4]
new_list = []
res = my_list[1::].__add__(my_list[:1])
print(res)

my_list = [1, 2, 3, 4]
first_pop = my_list.pop(0)
my_list.append(first_pop)
print(my_list)


val = "43 is grater than 34, but less than 56"
digit_list = []
val_replace = val.replace(",", " ")
# print(val_replace)
val_replace = val_replace.split(" ")
# print(val_replace)

for i in val_replace:
    if i.isdigit():
        digit_list.append(i)
# print(digit_list)
total = 0
for num in digit_list:
    total += int(num)
# res = sum(digit_list)
print(total)


val = "43 is grater than 34, but less than 56"
new_list = []

for i in val:
    if not i.isdigit():
        val=val.replace(i, " ")

new_list =val.split()
total = 0
# print(new_list)
for num in new_list:
    total+= int(num)
print(total)


val = "43 is grater than 34, but less than 56"
new_list = []

for word in val.split():
    if word.isdigit():
        new_list.append(int(word))
        # print(new_list)
    else:
        dig = ""
        for smbl in word:
            if smbl.isdigit():
                dig+=smbl

            else:
                if dig:
                    new_list.append((int(dig)))
                    dig =""

res = sum(new_list)
print(res)


val_1 = [2, 1, 1, 5, 3, 9, 0, 7]
count = 0
for i in range(1, len(val_1) - 1):
    if val_1[i] > val_1[i + 1] + val_1[i - 1]:
        count += 1

print(count)


my_list = [1, 2, 3, "11", '22', 33]
new_list = []
for i in my_list:
    if type(i) is str:
        new_list.append(i)
print(new_list)


my_str = "the Australian and New Zealand Standard Classification of Occupations (ANZSCO) code for each occupation. "
new_list = []
count = 0

for i in my_str:
    a = my_str.count(i)
    if a == 1:
        new_list.append(i)
print(new_list)


str_1 = "the Australian and New Zealand Standard Classification of Occupations (ANZSCO) code for each occupation. "
str_2 = "To learn more about us, please visit"
new_list = []

str_1_set = set(str_1)
str_2_set = set(str_2)
res = list(str_1_set.intersection(str_2_set))
new_list.extend(sorted(res))
print(new_list)


str_1 = "the Australian and New Zealand Standard Classification of Occupations (ANZSCO) code for each occupation. "
str_2 = "To learn more about us, please visit"
new_list = []

for i in str_1 and str_2:
    if i in str_1 and str_2:
        new_list.append(i)
print(new_list)



str_1 = "Pending nomination and/or visa applications will not be adversely impacted by the subsequent removal of any occupation from the skilled occupation lists."
str_2 = "To learn more about us, please visit"
new_list = []
count = 0
for i in str_1 and str_2:
    if i in str_1 and str_2 and str_1.count(i) == 1 and str_2.count(i) == 1:
        new_list.append(i)
print(new_list)


my_list = ["Beneficiaries who are not selected", "400", "Notification: Selected beneficiaries will be notified of their selection ", "401", 'This policy was approved', 'Criteria for Selection:']
new_list = []
print(new_list)

for j, k in enumerate(my_list):
    if j % 2 == 1:
        new_list.append(k[::-1])
    else:
        new_list.append(k)
print(new_list)

for j, k in enumerate(my_list):
    if j % 2 == 1:
        rev_str = k[::-1]
        new_list.append(rev_str)
    else:
        new_list.append(k)
print(new_list)


my_list = ["abc", "bca", "adv", "dva"]
new_list = [i for i in my_list if i.startswith("a")]
print(new_list)


my_list = ["abc", "bca", "adv", "dva"]
new_list = [i for i in my_list if i[0] == "a"]
print(new_list)


my_list = ["abc", "bca", "adv", "dva"]
for i in my_list:
    if i.startswith("a"):
        new_list.append(i)
print(new_list)


my_list = ["abc", "bca", "adv", "dva"]
for i in my_list:
    if i[0] == "a":
        new_list.append(i)
print(new_list)


my_list = ["hjk", "abc", "bca", "adv", "dva"]
new_list = []

for i in my_list:
    if "a" in i:
        new_list.append(i)
print(new_list)




{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict = {"key": "value",
           "address": "Dublin",
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
