#самостоятельная 1.3
#Задача 2
a=input()
print (a[1]) #второй символ строки
print(a[len(a)-2]) #пред символ в строке
print(a[:3]) #первые три символа
print(a[:len(a)-2]) #всю строчку кроме 2 последних символов
print(a[: :-2]) #все символы строке через 1 в обратном порядке
print(len(a)) #длина строки
""""#Задача 3
stroka = input("Строка: ")
simvol = input("Символ: ")
 n = []
 for i in stroka:
     if i ==simvol:
         n.append(i)
   print(len(n))
#Задача 4
korteg = (13, 2, 23, 14, 5)
for k in korteg:
    if k >10:
        print(str(k)+" ",end = " ")
        print(); input()"""