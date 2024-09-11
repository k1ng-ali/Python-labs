list = input('Введите число через пробел:').split()
list = [int(i) for i in list]
for i in range(len(list)):
    for j in range(i + 1, len(list)):

        list1_i = bin(list[i])
        list1_j = bin(list[j])
        list2_i = list1_i.count('1')
        list2_j = list1_j.count('1')
        if list2_i > list2_j or (list2_i == list2_j and list[i] > list[j]):
            list[i], list[j] = list[j], list[i]
        i_bin = list1_i[2:]

    print(list[i], " - ", i_bin)

print(list)
