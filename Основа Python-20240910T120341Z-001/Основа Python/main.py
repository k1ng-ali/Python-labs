with open("log.txt", "r") as file:  #Откроем файл log.txt для чтения
    n = int(file.readline())        #получаем информацию о количесве строк в первом строен
    code_count = {}
    for _ in range(n):
        code, mail = file.readline().split()    #Читаем по строчно и разделим по пробел
        if code in code_count:                  #Если код есть в листе прибавим единицу
            code_count[code] += 1
        else:                                   #Если нет добавим код в лист
            code_count[code] = 1

max_code = max(code_count, key=code_count.get)  #Находим код который использовалось больше раз

with open("log_code.txt", "w") as result:       #Резултать запишем в файл Log_code.txt
    result.write(max_code)

