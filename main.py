import random
kf_list2 = []
n = int(input(f'введите количетво неравенств- '))
for e in range(0, n):
    k = 0
    k = input('задайте степень многочлена - ')
    k = int(k)
    list_ = []
    kf = int(0)
    kf = random.randint(-100, 100)
    list_.append(f'{kf}*x')
    for i in range(1, k):
        kf = random.randint(-100, 100)
        if kf >= 0:
            list_.append(f'+{kf}*x**{i + 1}')
        else:
            list_.append(f'{kf}*x**{i + 1}')
    str1 = ''.join(list_)
    str2 = '=0'
    str4 = ''.join([str1, str2])
    print(str4)
    file = open(f"file{e}.txt", "w")
    file.write(f'{str4}')
    file.close()


for i in range(n):
    file = open(f"file{i}.txt")
    str5 = str
    str5 = file.read()

    str5 = str5.replace('=0', '').replace('+', " +").replace('-', ' -')

    str5 = str5.split()
    # print(str5)
    kf_list = []


    for i in str5:
        kf_list.append(int(i.split('*x')[0]))
    # print(kf_list)
    kf_list.extend([0, ] * (len(kf_list2) - len(kf_list)))
    kf_list2.extend([0, ] * (len(kf_list) - len(kf_list2)))
    # print(kf_list2)
    for i in range(len(kf_list2)):
        kf_list2[i]=(kf_list2[i] + kf_list[i])
# print(kf_list2)
strsum = str
file = open(f"filesum.txt", "w", encoding="utf-8")
for i in range(len(kf_list2)):
   strsum = (f'Сумма коэфициентов х**{i+1} равна {kf_list2[i]} \n')
   file.write(f'{strsum}')

file.close()
file = open(f"filesum.txt", "r", encoding="utf-8")
print(file.read())
file.close()

