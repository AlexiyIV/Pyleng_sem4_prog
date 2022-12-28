with open('H:/обучение/Python/семинары/Pyleng_sem4_prog/task_5_1.txt', 'r') as f1:
    data1 = f1.readline()
data11 = list(data1)
data11[-1] = ""
data11[-2] = ""
data1 = "".join(data11)
with open('H:/обучение/Python/семинары/Pyleng_sem4_prog/task_5_2.txt', 'r') as f2:
    data2 = f2.readline()
with open('H:/обучение/Python/семинары/Pyleng_sem4_prog/task_5_3.txt', 'w') as f3:
    f3.write(f'{data1}+{data2}\n')
print(data1[-1])
print(data1)
print(len(data1))