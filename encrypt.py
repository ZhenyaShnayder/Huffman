t=input("Введите путь к файлу ")
# 1.подсчет частот
# создание псевдо-ассоциативного массива
frequencies=[0 for i in range (256)]
try:
    f=open(t, "r")
except:
    print("Неправильно был указан путь файла ")
    exit()
sym=f.read(1)
while sym!='':
    frequencies[ord(sym)] +=1
    sym=f.read(1)
f.seek(0)
# 2.класс Uzel
class Uzel:
    #конструктор
    def __init__(self,sym, freq, left, right):
        self.freq=freq
        self.sym=sym
        self.left=left
        self.right=right
    def __repr__(self):
        return f"freq={self.freq}, sym={self.sym}, left={self.left}, right={self.right};"
#3.список узлов
str2=[]
for i in range (256):
    if frequencies[i]!=0:
        #создание узла
        str2.append(Uzel(chr(i), frequencies[i], None, None))
str3=str2.copy()
#4.сортировка списка узлов по частотам и построение дерева
#на место 0-го узла-новый добавляем в список, второй удаляем из списка
while(len(str2)>1):
    str2 = sorted(str2, key=lambda x: x.freq)# сортировка списка объектов по атрибуту: freq, создается lambda-функции, которая вернет freq объекта
    val1=str2[0]
    val2=str2[1]
    val=Uzel(-1, val1.freq+val2.freq, str2[0], str2[1])#присваиваем None-фиктивная вершина
    str2[0]=val
    str2.pop(1)
#5.рекурсивный обход дерева и создание словаря
dictionary={}#позволит хранить пары "ключ-значение", то есть будем хранить символы использованные в файле и в соответствие их кодировку в "0" и "1"
def Tree_traversal(str2, node):
    # str2=''#строка для хранения значений
    if (node.left is not None):
        Tree_traversal(str2+'0', node.left)
    if (node.right is not None):
        Tree_traversal(str2+'1', node.right)
    if (node.left is None and node.right is None):
        dictionary[node.sym] = str2
le=''
Tree_traversal(le, str2[0])
print(dictionary)

#узнаем сколько байт задействовано
d=0
for i in range (0,len(dictionary)):
    l=str3[i]
    d=l.freq+d
print("Сколько байт задействовано было бы без нашей кодировки: ",d)

#6.запись в файл 2 зашифрованное
t=input("Введите путь к файлу ")
try:
    f2=open(t, "wb")
except:
    print("Неправильно был указан путь файла ")
    exit()
# f2=open("C:\\Users\\днс\\OneDrive\\Рабочий стол\\encr.txt", "wb")
f2.write(chr(4).encode('ascii'))
for i in range(256):
    if(frequencies[i]!=0):
        f2.write(chr(i).encode("ascii"))
        f2.write(str(frequencies[i]).encode("ascii"))
        f2.write(chr(2).encode("ascii"))
f2.write(chr(3).encode("ascii"))
sym = f.read(1)
i=0
j=0
k=0
accum=0
while sym != '':
    code=dictionary[sym]
    accum=accum<<1
    i+=1
    if code[j]=='1':
        accum=accum|1
    j+=1
    if j==len(code):
        j=0
        sym=f.read(1)
    if i==7:
        f2.write(chr(accum).encode("ascii"))
        accum=0
        i=0
        k+=1
print("Сколько байт было задействовано:", k+1)
accum=accum<<7-i
f2.write(chr(accum).encode("ascii"))
f2.seek(0)
f2.write(chr(7-i).encode('ascii'))
f.close()
f2.close()